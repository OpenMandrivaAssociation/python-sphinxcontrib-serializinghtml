%define module sphinxcontrib_serializinghtml

Summary:	Serialized HTML file support for the Sphinx documentation generator
Name:		python-%(echo %{module}|sed -e 's,_,-,g')
Version:	2.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	ISC
Group:		Development/Python
Url:		https://sphinx-doc.org/
BuildArch:	noarch
BuildRequires:	gettext
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
Obsoletes:	python2-%{module} < 1.1.5

%description
Serialized HTML file support for the Sphinx documentation generator

%prep -a
find -name '*.mo' -delete

%build -p
for po in $(find -name '*.po'); do
  msgfmt --output-file=${po%.po}.mo ${po}
done

%install -a
# Move language files to /usr/share
cd %{buildroot}%{python_sitelib}
for lang in $(find sphinxcontrib/serializinghtml/locales -maxdepth 1 -mindepth 1 -type d -not -path '*/\.*' -printf "%f ");
do
  test $lang == __pycache__ && continue
  install -d %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES
  mv sphinxcontrib/serializinghtml/locales/$lang/LC_MESSAGES/*.mo %{buildroot}%{_datadir}/locale/$lang/LC_MESSAGES/
done
rm -rf sphinxcontrib/serializinghtml/locales
ln -s %{_datadir}/locale sphinxcontrib/serializinghtml/locales
cd -

%find_lang sphinxcontrib.serializinghtml

%files -f sphinxcontrib.serializinghtml.lang
%doc README.rst
%{python_sitelib}/sphinxcontrib/
%{python_sitelib}/*.*-info
