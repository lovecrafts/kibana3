.PHONY: help clean prepare signrpm signrepo
.DEFAULT: help
ifndef VERBOSE
.SILENT:
endif
SHELL=bash
CWD=$(shell pwd -P)
NAME=kibana3es5x
BUILD_NUMBER?=DEV
VERSION=0.$(shell date +%y%m%d).$(BUILD_NUMBER)
RELEASE=$(shell git log -n 1 --oneline|cut -c 1-7)
DONE = echo "====> $@ done"

help::
	echo -e "\nKibana3es5x packaging: Version \033[33m$(VERSION)\033[0m Release: \033[33m$(RELEASE)\033[0m\n"
	grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[33m%-20s\033[0m %s\n", $$1, $$2}'

prepare: clean $(NAME)-$(VERSION).tgz
	mkdir SRPMS RPMS SOURCES BUILD BUILDROOT
	cp $(NAME)-$(VERSION).tgz SOURCES/
	$(DONE)

KIBANA3=$(shell find ../src -type f)

$(KIBANA3):

$(NAME)-$(VERSION).tgz: $(KIBANA3)
	tar -czf $(NAME)-$(VERSION).tgz ../src/
	$(DONE)

srpm: prepare ## Build a source rpm
	sudo mock --buildsrpm --spec=$(CWD)/SPECS/$(NAME).spec --sources=$(CWD)/SOURCES/ --resultdir=$(CWD)/SRPMS --define "__version $(VERSION)" --define "__release $(RELEASE)"
	$(DONE)

rpm: srpm ## Build an rpm from the sourcerpm
	sudo mock --rebuild $(CWD)/SRPMS/$(NAME)*.src.rpm --resultdir=$(CWD)/RPMS/ --define "__version $(VERSION)" --define "__release $(RELEASE)"
	$(DONE)

clean: ## Clean up the workspace
	rm -rf RPMS SRPMS SOURCES BUILD BUILDROOT
	$(DONE)

devbuild: prepare ## Build a dev version, bypassing mock (useful for debugging RPM build issues)
	rpmbuild -ba --define "%_topdir $(CWD)" --define "__version $(VERSION)" --define "__release $(RELEASE)" $(CWD)/SPECS/$(NAME).spec
	$(DONE)

signrpm: ## Sign the rpm with the gpg key
	rpmsign --addsign $(CWD)/RPMS/$(NAME)-$(VERSION)-$(RELEASE).noarch.rpm
	$(DONE)

signrepo: ## Sign the repo key
	gpg --detach-sign --armor --yes repodata/repomd.xml
	$(DONE)
