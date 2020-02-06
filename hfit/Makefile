VERSION=0.1.6
PWD=$(shell pwd)

all: rpm clean

rpm:
	mkdir -p "$(PWD)/rpmbuild"
	mkdir -p "$(PWD)/rpmbuild/SOURCES/"
	cd "$(PWD)/rpmbuild" && mkdir -p "hfit-$(VERSION).linux-amd64" && cp SOURCES/hfit "hfit-$(VERSION).linux-amd64"
	cp -Rv contrib "$(PWD)/rpmbuild/hfit-$(VERSION).linux-amd64"
	cd "$(PWD)/rpmbuild" && tar cvfz hfit-$(VERSION).linux-amd64.tar.gz hfit-$(VERSION).linux-amd64
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -bb --clean contrib/hfit_sysvinit.spec
	rpmbuild --define '_topdir '"$(PWD)/rpmbuild" -bb --clean contrib/hfit_systemd.spec

deploy:
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=hfit.sysvinit -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/hfit/rpmbuild/RPMS/x86_64/hfit-$(VERSION)-sysvinit.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)
	curl -v -F r=$(REPOSITORY) -F hasPom=false -F e=rpm -F g=$(GROUPID) -F a=hfit.systemd -F v=$(VERSION) -F p=RPM -F file=@$(WORKSPACE)/hfit/rpmbuild/RPMS/x86_64/hfit-$(VERSION)-systemd.$(OS_NAME).x86_64.rpm -u $(REPOSITORY_CREDENTIALS) $(REPOSITORY_URL)

clean:
	rm -rf "$(PWD)/rpmbuild/SOURCES/hfit-$(VERSION)"
	rm -rf "$(PWD)/rpmbuild/SOURCES/hfit-$(VERSION).linux-amd64.tar.gz"
