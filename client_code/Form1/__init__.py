from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.
    self.drop_down_stocks.items = anvil.server.call('getTickers')

  def drop_down_stocks_change(self, **event_args):
    """This method is called when an item is selected"""
    #alert("You selecred a stock " + self.drop_down_stocks.selected_value)
    self.stockTicker.text = self.drop_down_stocks.selected_value
    self.stockPrice.text = anvil.server.call('getPrice')