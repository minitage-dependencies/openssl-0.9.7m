import os
from minitage.core.common import append_env_var


os_ldflags=''
uname=os.uname()[0]
if uname == 'Darwin':
    os_ldflags=' -mmacosx-version-min=10.5.0'

def patchopenssl(options,buildout):
    append_env_var('LDFLAGS', [' %s ' % os_ldflags,buildout['flags']['ldflags']],sep=' ',before=False)
    append_env_var('CFLAGS',  [buildout['flags']['cflags']],sep=' ',before=False)
    append_env_var('LD_RUN_PATH',  [buildout['flags']['ldrun']],sep=':',before=False)

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
