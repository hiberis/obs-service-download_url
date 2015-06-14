prefix = /usr

servicedir = ${prefix}/lib/obs/service

all:

install:
	install -d $(DESTDIR)$(servicedir)
	install -m 0755 download_url $(DESTDIR)$(servicedir)
	install -m 0644 download_url.service $(DESTDIR)$(servicedir)

.PHONY: all install
