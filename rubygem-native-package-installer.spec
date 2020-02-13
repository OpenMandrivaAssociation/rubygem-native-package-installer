
%define	gem_name	native-package-installer

Summary:	Ruby binding of cairo
Name:		rubygem-%{gem_name}

Version:	1.0.9
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:  rubygem(pkg-config)
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel

%description
A package installtion aid

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q -c -T  
# NOTE: Putting %%gem_install under the %%build tag will delete some files that should be installed.
%gem_install -n %{SOURCE0}

%build


%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{gem_dir} %{buildroot}%{gem_archdir}

cp -a .%{gem_dir}/* \
    %{buildroot}/%{gem_dir}/

%files
%{gem_dir}/gems/%{gem_name}-%{version}/lib/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/%{gem_name}/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/lib/%{gem_name}/platform/*.rb
%{gem_dir}/gems/%{gem_name}-%{version}/doc/text/[a-z]*
%{gem_dir}/gems/%{gem_name}-%{version}/test/*.rb
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%{gem_dir}/cache/*.gem


%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_dir}/gems/%{gem_name}-%{version}/[A-Z]*

