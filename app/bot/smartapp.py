"""Configuration for smartapp."""
from pybotx_smartapp_rpc import SmartAppRPC

from app.bot.rpc import methods

smartapp = SmartAppRPC(routers=[methods.rpc])
