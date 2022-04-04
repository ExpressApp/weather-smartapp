"""Configuration for smartapp."""
from botx_smartapp_rpc import SmartAppRPC

from app.bot.rpc import methods

smartapp = SmartAppRPC(routers=[methods.rpc])
