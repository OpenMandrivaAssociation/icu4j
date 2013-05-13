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

%global with_eclipse 1

%global section free

%global eclipse_base            %{_libdir}/eclipse
# Note:	this next section looks weird having an arch specified in a
# noarch specfile but the parts of the build
# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%global eclipse_arch    x86
%else
%global eclipse_arch   %{_arch}
%endif

Summary:	International Components for Unicode for Java
Name:		icu4j
Epoch:		1
Version:	4.4.2
Release:	4
License:	MIT and EPL 
Group:		Development/Java
Url:		http://site.icu-project.org/
#http://source.icu-project.org/repos/icu/icu4j/tags/release-4-4-2-eclipse37-20110208/ icu4j-4.4.2
#tar caf icu4j-4.4.2.tar.xz icu4j-4.4.2/
Source0:	icu4j-4.4.2.tar.xz
Source1:	%{name}-4.4.2.pom
Patch0:	%{name}-crosslink.patch

BuildRequires:	ant >= 1.7.0
# FIXME:	is this necessary or is it just adding strings in the hrefs in
# the docs?
BuildRequires:	java-javadoc >= 0:1.6.0
# This is to ensure we get OpenJDK and not GCJ
BuildRequires:	java-devel >= 0:1.6.0
BuildRequires:	jpackage-utils >= 0:1.5
Requires:	jpackage-utils
Requires(post,postun):	jpackage-utils
# This is to ensure we get OpenJDK and not GCJ
Requires:	java >= 0:1.6.0
%if %{with_eclipse}
BuildRequires:	eclipse-pde >= 0:3.2.1
%global         debug_package %{nil}
%else
BuildArch:	noarch
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
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	jpackage-utils
Requires:	java-javadoc >= 0:1.6.0

%description javadoc
Javadoc for %{name}.

%if %{with_eclipse}
%package eclipse
Summary:	Eclipse plugin for %{name}
Group:		Development/Java
Requires:	jpackage-utils

%description eclipse
Eclipse plugin support for %{name}.

%endif

%prep
%setup -q 
#%patch0 -p0

cp %{SOURCE1} .

%{__sed} -i 's/\r//' APIChangeReport.html
%{__sed} -i 's/\r//' readme.html

sed --in-place "s/ .*bootclasspath=.*//g" build.xml
sed --in-place "s/<date datetime=.*when=\"after\"\/>//" build.xml
sed --in-place "/javac1.3/d" build.xml
sed --in-place "s:/usr/lib:%{_libdir}:g" build.xml

%build
%ant -Dicu4j.javac.source=1.5 -Dicu4j.javac.target=1.5 -Dj2se.apidoc=%{_javadocdir}/java jar docs
%if %{with_eclipse}
pushd eclipse-build
  %ant -Dj2se.apidoc=%{_javadocdir}/java -Declipse.home=%{eclipse_base} \
    -Declipse.basews=gtk -Declipse.baseos=linux \
    -Declipse.basearch=%{eclipse_arch} \
    -Declipse.pde.dir=%{eclipse_base}/dropins/sdk/plugins/`ls %{eclipse_base}/dropins/sdk/plugins/|grep org.eclipse.pde.build_`
popd
%endif
  
%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp  -ap %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}-%{version}
cp  -pr doc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%if %{with_eclipse}
# eclipse
install -d -m755 %{buildroot}/%{eclipse_base}

unzip -qq -d %{buildroot}/%{eclipse_base} eclipse-build/out/projects/ICU4J.com.ibm.icu/com.ibm.icu-com.ibm.icu.zip
%endif

# maven stuff
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
cp %{name}-4.4.2.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap com.ibm.icu %{name} %{version} JPP %{name}

%post
%update_maven_depmap

%postun
%update_maven_depmap

%files
%doc readme.html APIChangeReport.html
%{_javadir}/%{name}*.jar
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom

%files javadoc
%doc %{_javadocdir}/*

%if %{with_eclipse}
%files eclipse
%dir %{_libdir}/eclipse
%dir %{_libdir}/eclipse/features
%dir %{_libdir}/eclipse/plugins
%{_libdir}/eclipse/features/*
%{_libdir}/eclipse/plugins/*
%doc readme.html
%endif

