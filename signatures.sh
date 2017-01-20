# Usage: sh signatures.sh  assethbox_VERSION.ova
echo MD5
md5sum $1
echo SHA1
sha1sum $1
echo SHA256
sha256sum $1
