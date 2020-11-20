# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin):
	def on_after_startup(self):
		self._logger.info("Hello World!")

	def get_settings_defaults(self):
		return dict(qp_copydir="smb://fileserver/data",
		    qp_localdir="/home/pi/.octoprint/watched",
		    qp_sufix="-nail.g")

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
			dict(type="tab", custom_bindings=False)
		]


__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
