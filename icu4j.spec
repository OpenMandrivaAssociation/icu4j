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

%define section free

%define eclipse_name            eclipse
%define eclipse_base            %{_libdir}/%{eclipse_name}

# Note:  this next section looks weird having an arch specified in a
# noarch specfile but the parts of the build
# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%define eclipse_arch    x86
%else
%define eclipse_arch   %{_arch}
%endif

Name:           icu4j
Version:        3.8.1
Release:        %mkrel 0.2.2
Epoch:          1
Summary:        International Components for Unicode for Java
License:        MIT and EPL
URL:            http://www-306.ibm.com/software/globalization/icu/index.jsp
Group:          Development/Java
Source0:        http://download.icu-project.org/files/icu4j/3.8.1/icu4j-3_8_1-src.jar
Patch0:         %{name}-crosslink.patch
# Set the OSGi shared configuration dir for our split (libdir and
# datadir) Eclipse packages.  Will go away once 3.4 is in.
Patch1:         %{name}-osgiconfigdir.patch
# Update the MANIFEST.MF to have the same qualifier in the bundle as is
# in Eclipse's Orbit project
Patch2:         %{name}-updatetimestamp.patch
# Bundle the source instead of having it be an exploded directory.  This
# doesn't work with a 3.3 Eclipse SDK but will with a 3.4 so we'll have
# to rebuild once we get 3.4 in.
Patch3:         %{name}-individualsourcebundle.patch
# PDE Build is in a location the upstream build.xml doesn't check
Patch4:         %{name}-pdebuildlocation.patch
BuildRequires:  ant
BuildRequires:  java-javadoc
BuildRequires:  java-rpmbuild >= 0:1.5
BuildRequires:  zip
Requires:       jpackage-utils
%if %{with_eclipse}
BuildRequires:  eclipse-pde >= 0:3.2.1
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

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
#%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%{__sed} -i 's/\r//' license.html
%{__sed} -i 's/\r//' APIChangeReport.html
%{__sed} -i 's/\r//' readme.html

sed --in-place "s/ .*bootclasspath=.*//g" build.xml
sed --in-place "s/<date datetime=.*when=\"after\"\/>//" build.xml
sed --in-place "/javac1.3/d" build.xml
sed --in-place "s:/usr/lib:%{_libdir}:g" build.xml

%build
%if %{without_eclipse}
%ant -Dicu4j.javac.source=1.5 -Dicu4j.javac.target=1.5 -Dj2se.apidoc=%{_javadocdir}/java jar docs
%else
%ant -Dj2se.apidoc=%{_javadocdir}/java -Declipse.home=%{eclipse_base} \
  -Declipse.basews=gtk -Declipse.baseos=linux \
  -Declipse.basearch=%{eclipse_arch} jar docs eclipsePDEBuild
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
install -d -m755 %{buildroot}/%{eclipse_base}

unzip -qq -d %{buildroot}/%{eclipse_base} eclipseProjects/ICU4J.com.ibm.icu/com.ibm.icu-com.ibm.icu.zip
%endif

%clean
%__rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc license.html readme.html APIChangeReport.html
%{_javadir}/%{name}*.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/*

%if %{with_eclipse}
%files eclipse
%defattr(0644,root,root,0755)
%dir %{_libdir}/eclipse
%dir %{_libdir}/eclipse/features
%dir %{_libdir}/eclipse/plugins
%{_libdir}/eclipse/features/*
%{_libdir}/eclipse/plugins/*
%doc license.html readme.html
%endif
