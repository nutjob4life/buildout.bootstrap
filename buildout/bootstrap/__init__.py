import urllib


def install(buildout):
    """
    You know, I have one simple request. And that is to have sharks with
    frickin' laser beams attached to their heads!

    Actually, all I really want to do is avoid typing:

        $ wget http://svn.zope.org/repos/main/zc.buildout/trunk/bootstrap/\
            bootstrap.py

    """
    url = 'http://svn.zope.org/repos/main/zc.buildout/%s/'
    url2 = 'bootstrap/bootstrap.py'
    version = 'trunk'
    url = url % version
    url = url + url2
    if 'bootstrap' in buildout:
        if 'version' in buildout['bootstrap']:
            version = buildout['bootstrap']['version']
            if version != 'trunk':
                version = 'tags/%s' % version
            url = url % version
            url = url + url2

    code = urllib.urlopen(url).getcode() 
    if code == 200:
        data = urllib.urlopen(url).read()
        file = '/'.join([buildout['buildout']['directory'], 'bootstrap.py'])
        bootstrap = open(file, 'w')
        bootstrap.write(data)
        bootstrap.close()

        print ('----------------------------------------' +
                '----------------------------------------')
        print 'Downloading zc.buildout bootstrap.py file from:\n  %s' % url
        print 'To:\n  %s' % file
        print ('----------------------------------------' +
                '----------------------------------------')
    elif code == 404:
        print ('----------------------------------------' +
                '----------------------------------------')
        print 'Unable to download zc.buildout bootstrap.py file from:\n  %s' % url
        print 'Not found.'
        print ('----------------------------------------' +
                '----------------------------------------')
    else:
        print ('----------------------------------------' +
                '----------------------------------------')
        print 'Unable to download zc.buildout bootstrap.py file from:\n  %s' % url
        print 'Unknown error code: %' % code
        print ('----------------------------------------' +
                '----------------------------------------')


