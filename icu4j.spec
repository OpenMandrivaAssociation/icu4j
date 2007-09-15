# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# If you want to build with eclipse support
# give rpmbuild option '--with eclipse'

%define _with_eclipse 1

%define with_eclipse %{?_with_eclipse:1}%{!?_with_eclipse:0}
%define without_eclipse %{!?_with_eclipse:1}%{?_with_eclipse:0}

%define _with_gcj_support 1

%define gcj_support %{?_with_gcj_support:1}%{!?_with_gcj_support:%{?_without_gcj_support:0}%{!?_without_gcj_support:%{?_gcj_support:%{_gcj_support}}%{!?_gcj_support:0}}}

%define section free

%define eclipse_name            eclipse
%define eclipse_base            %{_datadir}/%{eclipse_name}
%define eclipse_lib_base        %{_libdir}/%{eclipse_name}

Name:           icu4j
Version:        3.6.1
Release:        %mkrel 1.2.2
Epoch:          0
Summary:        International Components for Unicode for Java
License:        MIT style 
URL:            http://www-306.ibm.com/software/globalization/icu/index.jsp
Group:          Development/Java
Source0:        http://download.icu-project.org/files/icu4j/3.6.1/icu4jsrc_3_6_1.jar
Patch0:         %{name}-crosslink.patch
Patch1:         %{name}-disable-javadocs.patch
BuildRequires:  ant
BuildRequires:  java-javadoc
BuildRequires:  jpackage-utils >= 0:1.5
Requires:       jpackage-utils
%if %{with_eclipse}
BuildRequires:  eclipse-pde >= 0:3.2.1
%endif
%if ! %{gcj_support}
BuildArch:      noarch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
%if %{gcj_support}
BuildRequires:          java-gcj-compat-devel
%endif

%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving
performance, keeping current with the Unicode standard, and providing
richer APIs, while remaining as compatible as possible with the original
Java text and internationalization API design.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.

%if %{with_eclipse}
%package eclipse
Summary:        Eclipse plugin for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description eclipse
Eclipse plugin support for %{name}.

%endif

%prep
%setup -q -c
%patch0 -p0
%patch1 -p0

%{__sed} -i 's/\r//' license.html
%{__sed} -i 's/\r//' APIChangeReport.html
%{__sed} -i 's/\r//' readme.html

sed --in-place "s/ .*bootclasspath=.*//g" build.xml
sed --in-place "s/<date datetime=.*when=\"after\"\/>//" build.xml

%build
%if %{without_eclipse}
%ant -Dicu4j.javac.source=1.5 -Dicu4j.javac.target=1.5 -Dj2se.apidoc=%{_javadocdir}/java jar docs
%else
%ant -Dicu4j.javac.source=1.5 -Dicu4j.javac.target=1.5 -Dj2se.apidoc=%{_javadocdir}/java jar docs eclipseProjects
%endif

%if %{with_eclipse}
# eclipse build
export JAVA_HOME=%{java_home}
export PATH=%{java_bin}:/usr/bin:$PATH
    
# See comments in the script to understand this.
/bin/sh -x %{eclipse_base}/buildscripts/copy-platform SDK %{eclipse_base}
SDK=$(cd SDK >/dev/null && pwd)
    
# Eclipse may try to write to the home directory.
%__mkdir_p home

homedir=$(cd home > /dev/null && pwd)

pushd eclipseProjects
%{java} -cp $SDK/startup.jar \
     -Dosgi.sharedConfiguration.area=%{_libdir}/eclipse/configuration \
     -Duser.home=$homedir                        \
     org.eclipse.core.launcher.Main             \
     -application org.eclipse.ant.core.antRunner       \
     -Dtype=feature                                    \
     -Did=com.ibm.icu                                  \
     -DsourceDirectory=$(pwd)                          \
     -DbaseLocation=$SDK                               \
     -Dbuilder=%{eclipse_base}/plugins/org.eclipse.pde.build/templates/package-build  \
     -f %{eclipse_base}/plugins/org.eclipse.pde.build/scripts/build.xml

%endif

%install
%__rm -rf %{buildroot} 

# jars
%__mkdir_p %{buildroot}%{_javadir}
%__cp -ap %{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do %__ln_s ${jar} `echo $jar| sed "s|-%{version}||g"`; done)

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}-%{version}
%__cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%__ln_s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{with_eclipse}
# eclipse
install -d -m755 %{buildroot}/%{eclipse_lib_base}

pushd eclipseProjects
# FIXME: icu4j generates res_index.txt differently on different arches - possible libgcj bug.
unzip -qq -d %{buildroot}/%{_datadir}/ build/rpmBuild/com.ibm.icu.zip
popd

%endif

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
%__rm -rf %{buildroot}

%if %{gcj_support}
%post
%{update_gcjdb}
%endif

%if %{gcj_support}
%postun
%{clean_gcjdb}
%endif

%files
%defattr(0644,root,root,0755)
%doc license.html readme.html APIChangeReport.html
%{_javadir}/%{name}*.jar
%if %{gcj_support}
%dir %attr(-,root,root) %{_libdir}/gcj/%{name}/
%attr(-,root,root) %{_libdir}/gcj/%{name}/icu4j-%{version}.jar.*
%endif

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/*

%if %{with_eclipse}
%files eclipse
%defattr(0644,root,root,0755)
%dir %{_datadir}/eclipse
%dir %{_datadir}/eclipse/features
%dir %{_datadir}/eclipse/plugins
%{_datadir}/eclipse/features/*
%{_datadir}/eclipse/plugins/*
%doc license.html readme.html
%if %{gcj_support}
%{_libdir}/gcj/%{name}/com.ibm.icu*
%endif
%endif
