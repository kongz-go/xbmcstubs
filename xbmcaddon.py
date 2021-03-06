#noinspection PyUnusedLocal
class Addon(object):
    def __init__(self, id = None):
        """Creates a new Addon class.

        id: string - id of the addon (autodetected in XBMC Eden).

        Example:
            self.Addon = xbmcaddon.Addon(id='script.recentlyadded')
        """
        pass

    def getLocalizedString(self, id):
        """Returns an addon's localized 'unicode string'.

        id: integer - id# for string you want to localize.

        Example:
            locstr = self.Addon.getLocalizedString(id=6)
        """
        return unicode

    def getSetting(self, id):
        """Returns the value of a setting as a unicode string.

        id: string - id of the setting that the module needs to access.

        Example:
        apikey = self.Addon.getSetting('apikey')
        """
        return unicode

    def setSetting(self, id, value):
        """Sets a script setting.

        id: string - id of the setting that the module needs to access.
        value: string or unicode - value of the setting.

        Example:
            self.Settings.setSetting(id='username', value='teamxbmc')
        """
        pass

    def openSettings(self):
        """Opens this scripts settings dialog."""
        pass

    def getAddonInfo(self, id):
        """Returns the value of an addon property as a string.

        id: string - id of the property that the module needs to access.

        Note:
            Choices are (author, changelog, description, disclaimer, fanart, icon, id, name, path
            profile, stars, summary, type, version)

        Example:
            version = self.Addon.getAddonInfo('version')
        """
        return str
