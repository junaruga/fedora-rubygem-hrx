# Generated from hrx-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hrx

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 1%{?dist}
Summary: An HRX parser and serializer
License: ASL 2.0
URL: https://github.com/google/hrx-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3.0
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(linked-list)
BuildArch: noarch

%description
A parser and serializer for the HRX human-readable archive format.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Move the tests into place
ln -s %{_builddir}/spec spec
sed -i "/require 'rspec\/temp_dir'/ s/^/#/" spec/archive_spec.rb
sed -i '/^  context "::load" do$/,/^  end$/ s/^/#/' spec/archive_spec.rb
sed -i '/^  context "#write!" do$/,/^  end$/ s/^/#/' spec/archive_spec.rb
rspec -rspec_helper spec
popd


%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.rdoc_options
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/hrx.gemspec
%{gem_instdir}/spec

%changelog
* Tue Dec 03 2019 Leigh Scott <leigh123linux@gmail.com> - 1.0.0-1
- Initial package
