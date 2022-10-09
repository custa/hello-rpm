Name:       hello-rpm
Version:    1
Release:    2
Summary:    Most simple RPM package
License:    FIXME

%description
This is my first RPM package, which does nothing.

%prep
# we have no source, so nothing here

%build
cat > hello-rpm.sh <<EOF
#!/bin/bash
echo "Hello RPM"
EOF

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 hello-rpm.sh %{buildroot}/usr/bin/hello-rpm.sh

%files
/usr/bin/hello-rpm.sh

%changelog
# let's skip this for now
