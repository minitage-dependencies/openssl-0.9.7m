import os
from minitage.core.common import append_env_var

def patchopenssl(options,buildout):

    # if gmake is setted. taking it as the make cmd !
    # be careful to have a 'gmake' in your path
    if os.uname()[0] == 'FreeBSD':
        cmd1 = "gsed \
                -e 's|^FIPS_DES_ENC=|#FIPS_DES_ENC=|' \
                -e 's|^FIPS_SHA1_ASM_OBJ=|#FIPS_SHA1_ASM_OBJ=|' \
                -e 's|^SHLIB_EXT=.*$$|SHLIB_EXT=.so.$(SHLIBVER)|' \
                -e 's|fips-1.0||' \
                -e 's|^SHARED_LIBS_LINK_EXTS=.*$$|SHARED_LIBS_LINK_EXTS=.so|' \
                -e 's|^SHLIBDIRS= fips|SHLIBDIRS=|' \
                -i %s/*/Makefile" % (options['compile-directory'])

        if os.system(cmd1):
                raise Error('System error')


# vim:set ts=4 sts=4 et  :
