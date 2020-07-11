# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
wx.version()

import sys
from matplotlib import cm

# import gi
# gi.require_version('Gtk', '3.0')
# from gi.repository import Gtk
# from matplotlib.backends.backend_gtk3 import (NavigationToolbar2GTK3 as NavigationToolbar)

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.Point( 100,100 ), size = wx.Size( 740, 704 ), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		self.SetBackgroundColour( wx.Colour( 222, 222, 222 ) )
		
		MainSizer = wx.GridBagSizer( 0, 0 )
		MainSizer.SetFlexibleDirection( wx.BOTH )
		MainSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.domainGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.domainGrid.CreateGrid( 7, 1 )
		self.domainGrid.EnableEditing( True )
		self.domainGrid.EnableGridLines( True )
		self.domainGrid.EnableDragGridSize( False )
		self.domainGrid.SetMargins( 0, 0 )
		
		# Columns
		self.domainGrid.SetColSize( 0, 32 )
		self.domainGrid.EnableDragColMove( False )
		self.domainGrid.EnableDragColSize( True )
		self.domainGrid.SetColLabelSize( 0 )
		self.domainGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.domainGrid.EnableDragRowSize( True )
		self.domainGrid.SetRowLabelSize( 112 )
		self.domainGrid.SetRowLabelValue( 0, u"Length (m)" )
		self.domainGrid.SetRowLabelValue( 1, u"Height (m)" )
		self.domainGrid.SetRowLabelValue( 2, u"Airfoil Start (m)" )
		self.domainGrid.SetRowLabelValue( 3, u"Airfoil End (m)" )
		self.domainGrid.SetRowLabelValue( 4, u"NACA XXXX" )
		self.domainGrid.SetRowLabelValue( 5, u"Horizontal Cells" )
		self.domainGrid.SetRowLabelValue( 6, u"Vertical Cells" )
		self.domainGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.domainGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		MainSizer.Add( self.domainGrid, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.contourPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.contourPanel.SetBackgroundColour( wx.Colour( 222, 222, 222 ) )
		MainSizer.Add( self.contourPanel, wx.GBPosition( 0, 2 ), wx.GBSpan( 10, 54 ), wx.ALL|wx.EXPAND, 5 )
		
		self.consolePanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.consolePanel.SetBackgroundColour( wx.Colour( 222, 222, 222 ) )
		MainSizer.Add( self.consolePanel, wx.GBPosition( 14, 0 ), wx.GBSpan( 4, 60 ), wx.ALL|wx.EXPAND, 5 )

		# console redirecting
		self.consolePanel.command = wx.TextCtrl(self.consolePanel)
		self.consolePanel.result = wx.TextCtrl(self.consolePanel, style=wx.TE_MULTILINE)
		self.consolePanel.text = wx.TextCtrl(self.consolePanel, -1, style=wx.TE_MULTILINE|wx.TE_READONLY, size=(714, 50))
		redir=RedirectText(self.consolePanel.text)
		sys.stdout=redir
		
		self.iterPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.iterPanel.SetBackgroundColour( wx.Colour( 222, 222, 222 ) )
		
		MainSizer.Add( self.iterPanel, wx.GBPosition( 10, 2 ), wx.GBSpan( 4, 54 ), wx.ALL|wx.EXPAND, 5 )
		
		self.parameterGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.parameterGrid.CreateGrid( 4, 1 )
		self.parameterGrid.EnableEditing( True )
		self.parameterGrid.EnableGridLines( True )
		self.parameterGrid.EnableDragGridSize( False )
		self.parameterGrid.SetMargins( 0, 0 )
		
		# Columns
		self.parameterGrid.SetColSize( 0, 44 )
		self.parameterGrid.EnableDragColMove( False )
		self.parameterGrid.EnableDragColSize( True )
		self.parameterGrid.SetColLabelSize( 0 )
		self.parameterGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.parameterGrid.EnableDragRowSize( True )
		self.parameterGrid.SetRowLabelSize( 100 )
		self.parameterGrid.SetRowLabelValue( 0, u"Inlet Mach #" )
		self.parameterGrid.SetRowLabelValue( 1, u"Inlet Pres. (kPa)" )
		self.parameterGrid.SetRowLabelValue( 2, u"Inlet Temp. (K)" )
		self.parameterGrid.SetRowLabelValue( 3, u"< of Attack (°)" )
		self.parameterGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.parameterGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		MainSizer.Add( self.parameterGrid, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.simGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.simGrid.CreateGrid( 3, 1 )
		self.simGrid.EnableEditing( True )
		self.simGrid.EnableGridLines( True )
		self.simGrid.EnableDragGridSize( False )
		self.simGrid.SetMargins( 0, 0 )
		
		# Columns
		self.simGrid.SetColSize( 0, 44 )
		self.simGrid.EnableDragColMove( False )
		self.simGrid.EnableDragColSize( True )
		self.simGrid.SetColLabelSize( 0 )
		self.simGrid.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.simGrid.EnableDragRowSize( True )
		self.simGrid.SetRowLabelSize( 100 )
		self.simGrid.SetRowLabelValue( 0, u"Max. CFL" )
		self.simGrid.SetRowLabelValue( 1, u"Iterations" )
		self.simGrid.SetRowLabelValue( 2, u"Residual Tol." )
		self.simGrid.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.simGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		MainSizer.Add( self.simGrid, wx.GBPosition( 11, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Inlet Parameters", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		self.m_staticText11.SetForegroundColour(wx.Colour(0, 0, 0))

		MainSizer.Add( self.m_staticText11, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticText111 = wx.StaticText( self, wx.ID_ANY, u"Simulation Options", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText111.Wrap( -1 )
		self.m_staticText111.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		self.m_staticText111.SetForegroundColour(wx.Colour(0, 0, 0))
		
		MainSizer.Add( self.m_staticText111, wx.GBPosition( 10, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gridChoiceChoices = [ u"Wedge", u"Corner", u"Cylinder", u'NACA XXXX Airfoil', u'Biconvex Airfoil' ]
		self.gridChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, gridChoiceChoices, 0 )
		self.gridChoice.SetSelection( 3 )
		MainSizer.Add( self.gridChoice, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.schemeButton = wx.Button( self, wx.ID_ANY, u"Run Simulation", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.schemeButton, wx.GBPosition( 13, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		schemeChoiceChoices = [ u"AUSM", u"AUSM+up", u"AUSMDV", u"SLAU" ]
		self.schemeChoice = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, schemeChoiceChoices, 0 )
		self.schemeChoice.SetSelection( 0 )
		MainSizer.Add( self.schemeChoice, wx.GBPosition( 12, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.gridButton = wx.Button( self, wx.ID_ANY, u"Generate Grid", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.gridButton, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.initButton = wx.Button( self, wx.ID_ANY, u"Initialize", wx.DefaultPosition, wx.DefaultSize, 0 )
		MainSizer.Add( self.initButton, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Domain Parameters", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 10, 74, 90, 92, False, "Arial" ) )
		self.m_staticText1.SetForegroundColour(wx.Colour(0, 0, 0))
		
		MainSizer.Add( self.m_staticText1, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MainSizer.Add( self.m_staticline1, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		MainSizer.Add( self.m_staticline11, wx.GBPosition( 9, 0 ), wx.GBSpan( 1, 1 ), wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( MainSizer )
		self.Layout()
		self.menuBar = wx.MenuBar( 0 )
		self.menuBar.SetFont( wx.Font( 12, 74, 90, 90, False, "Arial" ) )

		self.gasOptions = wx.Menu()
		self.air = wx.MenuItem( self.gasOptions, 101, u"Air", wx.EmptyString, wx.ITEM_RADIO )
		self.gasOptions.Append( self.air )

		self.C02 = wx.MenuItem( self.gasOptions, 102, u"Carbon Dioxide", wx.EmptyString, wx.ITEM_RADIO )
		self.gasOptions.Append( self.C02 )

		self.H2 = wx.MenuItem( self.gasOptions, 103, u"Hydrogen", wx.EmptyString, wx.ITEM_RADIO )
		self.gasOptions.Append( self.H2 )
		
		self.gasOptions.AppendSeparator()
		
		self.thermalgas = wx.MenuItem( self.gasOptions, wx.ID_ANY, u"Thermally Perfect", wx.EmptyString, wx.ITEM_CHECK )
		self.gasOptions.Append( self.thermalgas )

		self.gasOptions.AppendSeparator()

		self.gasinfo = wx.MenuItem( self.gasOptions, wx.ID_ANY, u"Show More Information", wx.EmptyString, wx.ITEM_NORMAL )
		self.gasOptions.Append( self.gasinfo )
		self.menuBar.Append( self.gasOptions, u"Gas" ) 

		self.boundOptions = wx.Menu()
		self.botwall_invisc = wx.MenuItem( self.boundOptions, wx.ID_ANY, u"Bottom Wall: Inviscid Wall", wx.EmptyString, wx.ITEM_RADIO )
		self.boundOptions.Append( self.botwall_invisc )
		
		self.botwall_visc = wx.MenuItem( self.boundOptions, wx.ID_ANY, u"Bottom Wall: Viscous Wall", wx.EmptyString, wx.ITEM_RADIO )
		self.boundOptions.Append( self.botwall_visc )

		self.botwall_thermal = wx.Menu()
		self.botwall_adiabatic = wx.MenuItem( self.botwall_thermal, wx.ID_ANY, u"Adiabatic", wx.EmptyString, wx.ITEM_RADIO )
		self.botwall_thermal.Append( self.botwall_adiabatic )
		
		self.botwall_isothermal = wx.MenuItem( self.botwall_thermal, wx.ID_ANY, u"Isothermal", wx.EmptyString, wx.ITEM_RADIO )
		self.botwall_thermal.Append( self.botwall_isothermal )

		self.botwall_fixed = wx.MenuItem( self.botwall_thermal, wx.ID_ANY, u"Fixed Temperature", wx.EmptyString, wx.ITEM_RADIO )
		self.botwall_thermal.Append( self.botwall_fixed )
		
		self.boundOptions.AppendSubMenu( self.botwall_thermal, u"Bottom Wall Thermal Options" )

		self.boundOptions.AppendSeparator()

		self.topwall_out = wx.MenuItem( self.boundOptions, wx.ID_ANY, u"Top Wall: Outflow", wx.EmptyString, wx.ITEM_RADIO )
		self.boundOptions.Append( self.topwall_out )
		
		self.topwall_invisc = wx.MenuItem( self.boundOptions, wx.ID_ANY, u"Top Wall: Inviscid Wall", wx.EmptyString, wx.ITEM_RADIO )
		self.boundOptions.Append( self.topwall_invisc )
		
		self.topwall_visc = wx.MenuItem( self.boundOptions, wx.ID_ANY, u"Top Wall: Viscous Wall", wx.EmptyString, wx.ITEM_RADIO )
		self.boundOptions.Append( self.topwall_visc )

		self.topwall_thermal = wx.Menu()
		self.topwall_adiabatic = wx.MenuItem( self.topwall_thermal, wx.ID_ANY, u"Adiabatic", wx.EmptyString, wx.ITEM_RADIO )
		self.topwall_thermal.Append( self.topwall_adiabatic )
		
		self.topwall_isothermal = wx.MenuItem( self.topwall_thermal, wx.ID_ANY, u"Isothermal", wx.EmptyString, wx.ITEM_RADIO )
		self.topwall_thermal.Append( self.topwall_isothermal )

		self.topwall_fixed = wx.MenuItem( self.topwall_thermal, wx.ID_ANY, u"Fixed Temperature", wx.EmptyString, wx.ITEM_RADIO )
		self.topwall_thermal.Append( self.topwall_fixed )

		self.topwall_adiabatic.Enable(False)
		self.topwall_isothermal.Enable(False)
		self.topwall_fixed.Enable(False)
		
		self.boundOptions.AppendSubMenu( self.topwall_thermal, u"Top Wall Thermal Options" )
				
		self.menuBar.Append( self.boundOptions, u"Boundaries" ) 

		self.schemeOptions = wx.Menu()
		self.higherorder = wx.MenuItem( self.schemeOptions, wx.ID_ANY, u"Higher Order Accuracy?", wx.EmptyString, wx.ITEM_CHECK )
		self.schemeOptions.Append( self.higherorder )
		
		self.higherorderscheme = wx.Menu()
		self.secondfullupwind = wx.MenuItem( self.higherorderscheme, wx.ID_ANY, u"Second Order \"Full\" Upwind", wx.EmptyString, wx.ITEM_RADIO )
		self.higherorderscheme.Append( self.secondfullupwind )
		
		self.secondupwindbiased = wx.MenuItem( self.higherorderscheme, wx.ID_ANY, u"Second Order \"Full\" Upwind", wx.EmptyString, wx.ITEM_RADIO )
		self.higherorderscheme.Append( self.secondupwindbiased )
		
		self.secondcentral = wx.MenuItem( self.higherorderscheme, wx.ID_ANY, u"Second Order Central", wx.EmptyString, wx.ITEM_RADIO )
		self.higherorderscheme.Append( self.secondcentral )
		
		self.thirdfull = wx.MenuItem( self.higherorderscheme, wx.ID_ANY, u"Third Order \"Full\" Upwind", wx.EmptyString, wx.ITEM_RADIO )
		self.higherorderscheme.Append( self.thirdfull )
		
		self.thirdupwind = wx.MenuItem( self.higherorderscheme, wx.ID_ANY, u"Third Order Upwind", wx.EmptyString, wx.ITEM_RADIO )
		self.higherorderscheme.Append( self.thirdupwind )
		
		self.schemeOptions.AppendSubMenu( self.higherorderscheme, u"Higher Order Scheme" )
		
		self.limiterOptions = wx.Menu()
		self.minmod = wx.MenuItem( self.limiterOptions, wx.ID_ANY, u"Minmod", wx.EmptyString, wx.ITEM_RADIO )
		self.limiterOptions.Append( self.minmod )
		
		self.koren = wx.MenuItem( self.limiterOptions, wx.ID_ANY, u"Koren", wx.EmptyString, wx.ITEM_RADIO )
		self.limiterOptions.Append( self.koren )
		
		self.schemeOptions.AppendSubMenu( self.limiterOptions, u"Flux Limiter Function" )
		
		self.musclinfo = wx.MenuItem( self.schemeOptions, wx.ID_ANY, u"Show More Information", wx.EmptyString, wx.ITEM_NORMAL )
		self.schemeOptions.Append( self.musclinfo )
		
		self.menuBar.Append( self.schemeOptions, u"Scheme" ) 
		
		self.plotOptions = wx.Menu()
		self.contOptions = wx.Menu()
		self.mach = wx.MenuItem( self.contOptions, 1, u"Mach Number", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.mach )

		self.velocity = wx.MenuItem( self.contOptions, 2, u"Velocity", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.velocity )

		self.quiver = wx.MenuItem( self.contOptions, 3, u"Velocity Quiver", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.quiver )

		self.rho = wx.MenuItem( self.contOptions, 4, u"Density", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.rho )

		self.pressure = wx.MenuItem( self.contOptions, 5, u"Pressure", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.pressure )
		
		self.stagp = wx.MenuItem( self.contOptions, 6, u"Stagnation Pressure", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.stagp )
		
		self.temp = wx.MenuItem( self.contOptions, 7, u"Temperature", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.temp )
		
		self.stagtemp = wx.MenuItem( self.contOptions, 8, u"Stagnation Temperature", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.stagtemp )

		self.contOptions.AppendSeparator()

		self.coarse = wx.MenuItem( self.contOptions, 31, u"Coarse", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.coarse )
		
		self.medium = wx.MenuItem( self.contOptions, 32, u"Medium", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.medium )
		
		self.fine = wx.MenuItem( self.contOptions, 33, u"Fine", wx.EmptyString, wx.ITEM_RADIO )
		self.contOptions.Append( self.fine )

		self.contOptions.AppendSeparator()
		
		self.label = wx.MenuItem( self.contOptions, wx.ID_ANY, u"Contour Labels", wx.EmptyString, wx.ITEM_CHECK )
		self.contOptions.Append( self.label )

		self.gradient = wx.MenuItem( self.contOptions, wx.ID_ANY, u"Gradient", wx.EmptyString, wx.ITEM_CHECK )
		self.contOptions.Append( self.gradient )
		
		self.plotOptions.AppendSubMenu( self.contOptions, u"Contour Options" )
		
		self.cmOptions = wx.Menu()
		self.jet = wx.MenuItem( self.cmOptions, wx.ID_ANY, u"Jet", wx.EmptyString, wx.ITEM_RADIO )
		self.cmOptions.Append( self.jet )

		self.coolwarm = wx.MenuItem( self.cmOptions, wx.ID_ANY, u"CoolWarm", wx.EmptyString, wx.ITEM_RADIO )
		self.cmOptions.Append( self.coolwarm )

		self.seismic = wx.MenuItem( self.cmOptions, wx.ID_ANY, u"Seismic", wx.EmptyString, wx.ITEM_RADIO )
		self.cmOptions.Append( self.seismic )

		self.viridis = wx.MenuItem( self.cmOptions, wx.ID_ANY, u"Viridis", wx.EmptyString, wx.ITEM_RADIO )
		self.cmOptions.Append( self.viridis )

		self.magma = wx.MenuItem( self.cmOptions, wx.ID_ANY, u"Magma", wx.EmptyString, wx.ITEM_RADIO )
		self.cmOptions.Append( self.magma )
		
		self.gray = wx.MenuItem( self.cmOptions, wx.ID_ANY, u"Greyscale", wx.EmptyString, wx.ITEM_RADIO )
		self.cmOptions.Append( self.gray )
		
		self.plotOptions.AppendSubMenu( self.cmOptions, u"Colormap" )
		
		self.menuBar.Append( self.plotOptions, u"Plotting" ) 


		self.viewOptions = wx.Menu()
		self.expandCont = wx.MenuItem( self.viewOptions, wx.ID_ANY, u"Expand Contour Window", wx.EmptyString, wx.ITEM_NORMAL )
		self.viewOptions.Append( self.expandCont )

		self.axisOptions = wx.Menu()
		self.equal = wx.MenuItem( self.axisOptions, wx.ID_ANY, u"Equal", wx.EmptyString, wx.ITEM_RADIO )
		self.axisOptions.Append( self.equal )
		
		self.tight = wx.MenuItem( self.axisOptions, wx.ID_ANY, u"Tight", wx.EmptyString, wx.ITEM_RADIO )
		self.axisOptions.Append( self.tight )
		
		self.auto = wx.MenuItem( self.axisOptions, wx.ID_ANY, u"Auto", wx.EmptyString, wx.ITEM_RADIO )
		self.axisOptions.Append( self.auto )
		
		self.viewOptions.AppendSubMenu( self.axisOptions, u"Axis Options" )
		
		self.menuBar.Append( self.viewOptions, u"View" ) 

		
		self.unitOptions = wx.Menu()
		
		self.metric1 = wx.MenuItem( self.unitOptions, wx.ID_ANY, u"Metric (kg-m-s-K)", wx.EmptyString, wx.ITEM_RADIO )
		self.unitOptions.Append( self.metric1 )

		self.metric2 = wx.MenuItem( self.unitOptions, wx.ID_ANY, u"Metric (kg-m-s-°C)", wx.EmptyString, wx.ITEM_RADIO )
		self.unitOptions.Append( self.metric2 )

		self.imperial1 = wx.MenuItem( self.unitOptions, wx.ID_ANY, u"Imperial (lbm-ft-s-°F)", wx.EmptyString, wx.ITEM_RADIO )
		self.unitOptions.Append( self.imperial1 )

		self.imperial2 = wx.MenuItem( self.unitOptions, wx.ID_ANY, u"Imperial (slug-in-s-°R)", wx.EmptyString, wx.ITEM_RADIO )
		self.unitOptions.Append( self.imperial2 )
		
		self.menuBar.Append( self.unitOptions, u"Units" ) 
		
		self.SetMenuBar( self.menuBar )
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.schemeButton.Bind( wx.EVT_BUTTON, self.call_scheme )
		self.gridButton.Bind( wx.EVT_BUTTON, self.call_grid )
		self.initButton.Bind( wx.EVT_BUTTON, self.call_init )

		self.gridChoice.Bind( wx.EVT_CHOICE, self.grid_change )


		self.Bind( wx.EVT_MENU, self.gas_change, id = self.air.GetId() )
		self.Bind( wx.EVT_MENU, self.gas_change, id = self.C02.GetId() )
		self.Bind( wx.EVT_MENU, self.gas_change, id = self.H2.GetId() )
		self.Bind( wx.EVT_MENU, self.thermalgas_change, id = self.thermalgas.GetId() )
		self.Bind( wx.EVT_MENU, self.infoWindow, id = self.gasinfo.GetId() )

		self.Bind( wx.EVT_MENU, self.topwall_change, id = self.topwall_out.GetId() )
		self.Bind( wx.EVT_MENU, self.topwall_change, id = self.topwall_invisc.GetId() )
		self.Bind( wx.EVT_MENU, self.topwall_change, id = self.topwall_visc.GetId() )

		self.Bind( wx.EVT_MENU, self.botwall_thermal_change, id = self.botwall_isothermal.GetId() )
		self.Bind( wx.EVT_MENU, self.botwall_thermal_change, id = self.botwall_fixed.GetId() )
		self.Bind( wx.EVT_MENU, self.topwall_thermal_change, id = self.topwall_isothermal.GetId() )
		self.Bind( wx.EVT_MENU, self.topwall_thermal_change, id = self.topwall_fixed.GetId() )

		self.Bind( wx.EVT_MENU, self.cont_change, id = self.mach.GetId() )
		self.Bind( wx.EVT_MENU, self.cont_change, id = self.velocity.GetId() )
		self.Bind( wx.EVT_MENU, self.cont_change, id = self.quiver.GetId() )
		self.Bind( wx.EVT_MENU, self.cont_change, id = self.rho.GetId() )
		self.Bind( wx.EVT_MENU, self.cont_change, id = self.pressure.GetId() )
		self.Bind( wx.EVT_MENU, self.cont_change, id = self.stagp.GetId() )
		self.Bind( wx.EVT_MENU, self.cont_change, id = self.temp.GetId() )
		self.Bind( wx.EVT_MENU, self.cont_change, id = self.stagtemp.GetId() )
		self.Bind( wx.EVT_MENU, self.contlevel_change, id = self.coarse.GetId() )
		self.Bind( wx.EVT_MENU, self.contlevel_change, id = self.medium.GetId() )
		self.Bind( wx.EVT_MENU, self.contlevel_change, id = self.fine.GetId() )
		self.Bind( wx.EVT_MENU, self.label_change, id = self.label.GetId() )
		self.Bind( wx.EVT_MENU, self.gradient_change, id = self.gradient.GetId() )
		self.Bind( wx.EVT_MENU, self.cm_change, id = self.jet.GetId() )
		self.Bind( wx.EVT_MENU, self.cm_change, id = self.coolwarm.GetId() )
		self.Bind( wx.EVT_MENU, self.cm_change, id = self.seismic.GetId() )
		self.Bind( wx.EVT_MENU, self.cm_change, id = self.viridis.GetId() )
		self.Bind( wx.EVT_MENU, self.cm_change, id = self.magma.GetId() )
		self.Bind( wx.EVT_MENU, self.cm_change, id = self.gray.GetId() )
		self.Bind( wx.EVT_MENU, self.unit_change, id = self.metric1.GetId())
		self.Bind( wx.EVT_MENU, self.unit_change, id = self.metric2.GetId())
		self.Bind( wx.EVT_MENU, self.unit_change, id = self.imperial1.GetId())
		self.Bind( wx.EVT_MENU, self.unit_change, id = self.imperial2.GetId())
		self.Bind( wx.EVT_MENU, self.expandWindow, id = self.expandCont.GetId() )
		self.Bind( wx.EVT_MENU, self.axis_change, id = self.equal.GetId() )
		self.Bind( wx.EVT_MENU, self.axis_change, id = self.tight.GetId() )
		self.Bind( wx.EVT_MENU, self.axis_change, id = self.auto.GetId() )


		# initialize grid values and class attributes
		self.init_grids()

		class options:
			self.contQuantity = 'Mach'
		self.cmOption = cm.jet
		class units:
			mass = 'kg'
			def conv_mass(m):
				conv = m
				return conv
			length = 'm'
			def conv_length(l):
				conv = l
				return conv
			time = 's'
			def conv_time(t):
				conv = t
				return conv
			temp = 'K'
			def conv_temp(T):
				conv = T
				return conv
			press = 'kPa'
			def conv_press(p):
				conv = p / 1000
				return conv
			energy = 'J'
			def conv_energy(e):
				conv = e
				return conv
		self.units = units
		self.axisOption = 'equal'
		self.contGrad = 512
		self.labeled = False
		self.gradient = ''
		self.gasSelect = 'Air'
		self.thermoModel = 'cpg'


	def __del__( self ):
		pass


	# initialize option grid values
	def init_grids( self ):
		# set domain row values
		self.domainGrid.SetCellValue( 0, 0, "1.5")
		self.domainGrid.SetCellValue( 1, 0, "1.3")
		self.domainGrid.SetCellValue( 2, 0, "0.5")
		self.domainGrid.SetCellValue( 3, 0, "1.1")
		self.domainGrid.SetCellValue( 4, 0, "0012")
		self.domainGrid.SetCellValue( 5, 0, "48")
		self.domainGrid.SetCellValue( 6, 0, "36")

		# set initialization row values
		self.parameterGrid.SetCellValue( 0, 0, "3.0")
		self.parameterGrid.SetCellValue( 1, 0, "101.325")
		self.parameterGrid.SetCellValue( 2, 0, "300")
		self.parameterGrid.SetCellValue( 3, 0, "0")

		# set initialization row values
		self.simGrid.SetCellValue( 0, 0, "0.4")
		self.simGrid.SetCellValue( 1, 0, "1000")
		self.simGrid.SetCellValue( 2, 0, "-6")

		# set contour gradient to fine
		self.contOptions.Check(33, True)


	# Virtual event handlers, overide them in your derived class
	def call_grid( self, event ):
		import numpy as np
		from python.mesh.grid.gen_grid import mesh_wedge, mesh_corner, mesh_cylinder, mesh_naca4, mesh_biconvex
		from python.mesh.metrics.calc_cell_metrics import cellmetrics
		import matplotlib.pyplot as plt
		import matplotlib as mpl
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
		from pytictoc import TicToc

		t = TicToc()
		t.tic()

		# length unit conversion
		cl = self.units.conv_length(1)

		class domain:
			name = self.gridChoice.Strings[self.gridChoice.Selection]
			M = int(wx.grid.Grid.GetCellValue(self.domainGrid, 5, 0))
			N = int(wx.grid.Grid.GetCellValue(self.domainGrid, 6, 0))
			obj_start = float(wx.grid.Grid.GetCellValue(self.domainGrid, 2, 0)) / cl
			obj_end = float(wx.grid.Grid.GetCellValue(self.domainGrid, 3, 0)) / cl
			length = float(wx.grid.Grid.GetCellValue(self.domainGrid, 0, 0)) / cl
			height = float(wx.grid.Grid.GetCellValue(self.domainGrid, 1, 0)) / cl
			if name == 'NACA XXXX Airfoil':
				naca = wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0)
				alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))
			elif name == 'Biconvex Airfoil':
				thickness = float(wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0))
				alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))
			else:
				theta = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0)))
				alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))

		if domain.name == "Wedge":
			xx, yy = mesh_wedge(domain)
		elif domain.name == "Corner":
			xx, yy = mesh_corner(domain)
		elif domain.name == "Cylinder":
			xx, yy = mesh_cylinder(domain)
		elif domain.name == "NACA XXXX Airfoil":
			xx, yy = mesh_naca4(domain)
		elif domain.name == "Biconvex Airfoil":
			xx, yy = mesh_biconvex(domain)
		self.mesh = cellmetrics(xx, yy, domain)
		# self.mesh.xxp = self.mesh.xxc
		# self.mesh.yyp = self.mesh.yyc
		self.domain = domain

		# if hasattr(self.mesh, 'alpha')
    	# 	rot.rotate(self.mesh.xxp, self.mesh.yyp, -self.domain.alpha, domain.M+2, domain.N+2)

		print('________________________________________________________________________________________________________________________________________')
		print('Mesh elements: ' + str((domain.M+2) * (domain.N*2)))
		t.toc('Meshing time:')

		# mesh plotting
		plt.close(fig=self.contourPanel.figure)
		self.contourPanel.figure = plt.figure( dpi=100, figsize=(5.6, 4), facecolor=(222/256,222/256,222/256) )
		self.contourPanel.cax = self.contourPanel.figure.gca()
		self.contourPanel.cax.set_position([0.08, 0.11, 0.84, 0.78])

		#mpl.axes.Axes.clear(self.contourPanel.cax)
		self.contourPanel.cax.plot(self.mesh.xx * cl, self.mesh.yy * cl, color='blue', linewidth=0.5)
		self.contourPanel.cax.plot(np.transpose(self.mesh.xx) * cl, np.transpose(self.mesh.yy) * cl, color='blue', linewidth=0.5)
		self.contourPanel.cax.plot(self.mesh.xxc * cl, self.mesh.yyc * cl, 'gx', markersize=0.25)

		# plot settings
		if self.topwall_out.IsChecked():
			self.contourPanel.cax.set(xlim=[np.min(self.mesh.xx) * cl, np.max(self.mesh.xx) * cl], \
					  	  			  ylim=[np.min(self.mesh.yy) * cl, np.max(self.mesh.yy) * cl])
		else:
			self.contourPanel.cax.set(xlim=[np.min(self.mesh.xx) * cl, np.max(self.mesh.xx) * cl], \
					  	  			  ylim=[np.min(self.mesh.yy[:,0:-1]) * cl, np.max(self.mesh.yy[:,0:-1]) * cl])

		self.contourPanel.cax.set_xlabel('x-coordinate ' + '(' + self.units.length + ')')
		self.contourPanel.cax.set_ylabel('y-coordinate ' + '(' + self.units.length + ')')
		self.contourPanel.cax.set_aspect(self.axisOption, adjustable='box', anchor='C')
		self.contourPanel.canvas = FigureCanvas(self.contourPanel, -1, self.contourPanel.figure)

		sizer = wx.BoxSizer(wx.HORIZONTAL)
		sizer.Add(self.contourPanel.canvas, proportion=1, flag=wx.LEFT | wx.TOP | wx.GROW)
		self.SetSizer(sizer)

		event.Skip()

	def call_init( self, event ):
		import numpy as np
		from python.mesh.grid.gen_grid import mesh_wedge, mesh_corner, mesh_cylinder
		from python.mesh.metrics.calc_cell_metrics import cellmetrics
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
		from pytictoc import TicToc
		import python.finite_volume.gasdata as gasdata

		t = TicToc()

		if self.domain.name == 'NACA XXXX Airfoil':
			self.domain.naca = wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0)
			self.domain.alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))
		elif self.domain.name == 'Biconvex Airfoil':
			self.domain.thickness = float(wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0))
			self.domain.alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))
		else:
			self.domain.theta = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0)))
			self.domain.alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))

		# initialize state vector, simulation parameters and fluid properties
		class parameters:
			M_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 0, 0))
			p_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 1, 0)) / self.units.conv_press(1)
			if self.units.temp == '°C':
				T_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 2, 0)) + self.units.conv_temp(0)
			elif self.units.temp == '°F':
				T_in = (float(wx.grid.Grid.GetCellValue(self.parameterGrid, 2, 0))-32)*(5/9) + 273.15
			else:
				T_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 2, 0)) * self.units.conv_temp(1)

			iterations = int(wx.grid.Grid.GetCellValue(self.simGrid, 1, 0))
			tolerance = float(wx.grid.Grid.GetCellValue(self.simGrid, 2, 0))
			CFL = float(wx.grid.Grid.GetCellValue(self.simGrid, 0, 0))
			if self.topwall_out.IsChecked():
				topwall = 'Outflow'
			elif self.topwall_visc.IsChecked():
				topwall = 'Viscous Wall'
			elif self.topwall_invisc.IsChecked():
				topwall = 'Inviscid Wall'
			if self.topwall_adiabatic.IsChecked():
				topwall_thermal = 'Adiabatic'
			elif self.topwall_isothermal.IsChecked():
				topwall_thermal = 'Isothermal'
				topwall_temp = self.units.conv_temp(float(self.top_thermal_window.walltemp))
			elif self.topwall_fixed.IsChecked():
				topwall_thermal = 'Fixed Temperature'
				topwall_temp = self.units.conv_temp(float(self.top_thermal_window.walltemp))

			if self.botwall_visc.IsChecked():
				botwall = 'Viscous Wall'
			elif self.botwall_invisc.IsChecked():
				botwall = 'Inviscid Wall'
			if self.botwall_adiabatic.IsChecked():
				botwall_thermal = 'Adiabatic'
			elif self.botwall_isothermal.IsChecked():
				botwall_thermal = 'Isothermal'
				botwall_temp = self.units.conv_temp(float(self.bot_thermal_window.walltemp))
			elif self.botwall_fixed.IsChecked():
				botwall_thermal = 'Fixed Temperature'
				botwall_temp = self.units.conv_temp(float(self.bot_thermal_window.walltemp))

		self.parameters = parameters
		self.gas = gasdata.air_tpg

		# initialize state vector, thermodynamic variables
		t.tic()
		from python.boundary.initialize import init_state
		self.state = init_state(self.domain, self.mesh, self.parameters, self.gas)

		print('________________________________________________________________________________________________________________________________________')
		t.toc('Initialize time:')

		self.call_contplot(self.contourPanel, 1, 1)

		event.Skip()

	def call_scheme( self, event ):

		import numpy as np
		from pytictoc import TicToc
		from python.finite_volume.AUSM.schemes import AUSM, AUSMmuscl, AUSMplusup, AUSMDV, SLAU
		import python.finite_volume.gasdata as gasdata

		t = TicToc()

		# run AUSM family scheme
		t.tic()
		scheme = self.schemeChoice.Strings[self.schemeChoice.Selection]

		if self.domain.name == 'NACA XXXX Airfoil':
			self.domain.naca = wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0)
			self.domain.alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))
		elif self.domain.name == 'Biconvex Airfoil':
			self.domain.thickness = float(wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0))
			self.domain.alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))
		else:
			self.domain.theta = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.domainGrid, 4, 0)))
			self.domain.alpha = np.deg2rad(float(wx.grid.Grid.GetCellValue(self.parameterGrid, 3, 0)))

		class parameters:
			M_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 0, 0))
			p_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 1, 0)) / self.units.conv_press(1)
			if self.units.temp == '°C':
				T_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 2, 0)) + self.units.conv_temp(0)
			elif self.units.temp == '°F':
				T_in = (float(wx.grid.Grid.GetCellValue(self.parameterGrid, 2, 0))-32)*(5/9) + 273.15
			else:
				T_in = float(wx.grid.Grid.GetCellValue(self.parameterGrid, 2, 0)) * self.units.conv_temp(1)
			iterations = int(wx.grid.Grid.GetCellValue(self.simGrid, 1, 0))
			tolerance = float(wx.grid.Grid.GetCellValue(self.simGrid, 2, 0))
			CFL = float(wx.grid.Grid.GetCellValue(self.simGrid, 0, 0))
			if self.topwall_out.IsChecked():
				topwall = 'Outflow'
			elif self.topwall_visc.IsChecked():
				topwall = 'Viscous Wall'
			elif self.topwall_invisc.IsChecked():
				topwall = 'Inviscid Wall'
			if self.topwall_adiabatic.IsChecked():
				topwall_thermal = 'Adiabatic'
			elif self.topwall_isothermal.IsChecked():
				topwall_thermal = 'Isothermal'
				topwall_temp = self.units.conv_temp(float(self.top_thermal_window.walltemp))
			elif self.topwall_fixed.IsChecked():
				topwall_thermal = 'Fixed Temperature'
				topwall_temp = self.units.conv_temp(float(self.top_thermal_window.walltemp))

			if self.botwall_visc.IsChecked():
				botwall = 'Viscous Wall'
			elif self.botwall_invisc.IsChecked():
				botwall = 'Inviscid Wall'
			if self.botwall_adiabatic.IsChecked():
				botwall_thermal = 'Adiabatic'
			elif self.botwall_isothermal.IsChecked():
				botwall_thermal = 'Isothermal'
				botwall_temp = self.units.conv_temp(float(self.bot_thermal_window.walltemp))
			elif self.botwall_fixed.IsChecked():
				botwall_thermal = 'Fixed Temperature'
				botwall_temp = self.units.conv_temp(float(self.bot_thermal_window.walltemp))

		self.parameters = parameters

		if self.thermoModel == 'cpg':
			if self.air.IsChecked() == True:
				self.gas = gasdata.air_cpg
			elif self.C02.IsChecked() == True:
				self.gas = gasdata.C02_cpg
			elif self.H2.IsChecked() == True:
				self.gas = gasdata.H2_cpg
		elif self.thermoModel == 'tpg':
			if self.air.IsChecked() == True:
				self.gas = gasdata.air_tpg
			elif self.C02.IsChecked() == True:
				self.gas = gasdata.C02_tpg
			elif self.H2.IsChecked() == True:
				self.gas = gasdata.H2_tpg
		
		if scheme == 'AUSM':
			if self.higherorder.IsChecked():
				self.state = AUSMmuscl( self.domain, self.mesh, self.parameters, self.state, self.gas )
			else:
				self.state = AUSM( self.domain, self.mesh, self.parameters, self.state, self.gas )
		elif scheme == 'AUSM+up':
			self.state = AUSMplusup( self.domain, self.mesh, self.parameters, self.state, self.gas )
		elif scheme == 'AUSMDV':
			self.state = AUSMDV( self.domain, self.mesh, self.parameters, self.state, self.gas )
		elif scheme == 'SLAU':
			self.state = SLAU( self.domain, self.mesh, self.parameters, self.state, self.gas )

		t.toc('simulation time:')

		self.call_contplot(self.contourPanel, 1, 1)
		self.call_resplot()

		event.Skip()

	def call_contplot(self, panel, scalex, scaley):

		import numpy as np
		import matplotlib.pyplot as plt
		from matplotlib import cm
		import matplotlib as mpl
		import matplotlib.pyplot as plt
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
		import matplotlib.ticker as ticker

		# panel input as self.contourPanel

		# length to height ratio
		r = min(1, (1.35/1.3) / ( ( np.max(self.mesh.xxc) - np.min(self.mesh.xxc) ) / \
							   ( np.max(self.mesh.yyc - np.min(self.mesh.yyc) ) ) ) )
		
		# post processing
		plt.close(fig=panel.figure)
		if scalex > 1 or scaley > 1:
			panel.figure = plt.figure( dpi=100, figsize=(scalex*5.6, scaley*4.2), facecolor=(1, 1, 1) )
		else:
			panel.figure = plt.figure( dpi=100, figsize=(scalex*5.6, scaley*4.2), facecolor=(222/256,222/256,222/256) )

		panel.cax = panel.figure.gca()
		panel.cax.set_facecolor((0.4, 0.4, 0.4))
		panel.cax.set_position([0.12, 0.22, 0.84, 0.8], which='both')
		
		contQuantity = self.contQuantity + ' ' + self.gradient
		cl = self.units.conv_length(1)

		if contQuantity == 'Mach ':
			cont = panel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
							    		      	  self.state.Mach[0:-1,1:-1], self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(self.state.Mach),2), round(np.max(self.state.Mach),2), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity, rotation=90)
		elif contQuantity == 'Velocity ':
			velocity = (cl/self.units.conv_time(1)) * self.state.vel[0:-1,1:-1]
			cont = panel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
							    		      	  velocity, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(velocity),0), round(np.max(velocity),0), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.length + '/' + self.units.time + ')', rotation=90)
		elif contQuantity == 'Velocity Quiver ':
			downM = int(self.domain.M/24)
			downN = int(self.domain.N/24)
			fill = panel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
									  self.state.Mach[0:-1,1:-1] * 0, colors='w')
			cont = panel.cax.quiver(cl*self.mesh.xxc[0:-1:downM,1:-1:downN], cl*self.mesh.yyc[0:-1:downM,1:-1:downN], \
								  				self.state.u[0:-1:downM,1:-1:downN], self.state.v[0:-1:downM,1:-1:downN], \
												self.state.vel[0:-1:downM,1:-1:downN], cmap=self.cmOption, pivot='tip', \
												angles='uv', scale_units='width', \
												scale=0.8*self.domain.M*np.max(self.state.vel[0:-1,1:-1])/max((downM,downM)))
			# colorbar settings
			ticks = np.linspace(round(np.min(self.state.vel),0), round(np.max(self.state.vel),0), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.length + '/' + self.units.time + ')', rotation=90)
		elif contQuantity == 'Density ':
			rho = self.units.conv_mass(1)/self.units.conv_length(1)**3
			cont = panel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
							    		      	  rho*self.state.Q[0:-1,1:-1,0], self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(rho*self.state.Q[0:-1,1:-1,0]),9), round(np.max(rho*self.state.Q[0:-1,1:-1,0]),9), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.mass + '/' + self.units.length + '$^3$' + ')', rotation=90)
		elif contQuantity == 'Density Gradient':
			from python.finite_volume.helper import grad
			rho = self.units.conv_mass(1)/self.units.conv_length(1)**4
			rhograd = grad(cl*self.mesh.xxc, cl*self.mesh.yyc, rho*self.state.Q[:,:,0])
			cont = panel.cax.contourf(cl*self.mesh.xxc[1:-1,1:-1], cl*self.mesh.yyc[1:-1,1:-1], \
							    		      	  rhograd, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(rhograd), 9), round(np.max(rhograd), 9), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.mass + '/' + self.units.length + '$^4$' + ')', rotation=90)
		elif contQuantity == 'Pressure ':
			pressure = self.units.conv_press(self.state.p[0:-1,1:-1])
			cont = panel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
							    		      	  pressure, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(pressure),0), round(np.max(pressure),0), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.press + ')', rotation=90)
		elif contQuantity == 'Pressure Gradient':
			from python.finite_volume.helper import grad
			pg = self.units.conv_press(1) / self.units.conv_length(1)
			pgrad = grad(cl*self.mesh.xxc, cl*self.mesh.yyc, pg*self.state.p)
			cont = panel.cax.contourf(cl*self.mesh.xxc[1:-1,1:-1], cl*self.mesh.yyc[1:-1,1:-1], \
							    		      	  pgrad, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(pgrad), 9), round(np.max(pgrad), 9), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.press + '/' + self.units.length + ')', rotation=90)
		elif contQuantity == 'Stagnation Pressure ':
			p0 = self.units.conv_press(self.state.p0[0:-1,1:-1])
			cont = self.contourPanel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
							    		      	  p0, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(p0),0), round(np.max(p0),0), 6)
			CB = self.contourPanel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.press + ')', rotation=90)
		elif contQuantity == 'Temperature ':
			temperature = self.units.conv_temp(self.state.T[0:-1,1:-1])
			cont = panel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
							    		      	  temperature, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(temperature),0), round(np.max(temperature),0), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.temp + ')', rotation=90)
		elif contQuantity == 'Temperature Gradient':
			from python.finite_volume.helper import grad
			ct = self.units.conv_temp(1) / self.units.conv_length(1)
			tgrad = grad(cl*self.mesh.xxc, cl*self.mesh.yyc, ct*self.state.T)
			cont = panel.cax.contourf(cl*self.mesh.xxc[1:-1,1:-1], cl*self.mesh.yyc[1:-1,1:-1], \
							    		      	  tgrad, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(tgrad), 0), round(np.max(tgrad), 0), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.temp + '/' + self.units.length + ')', rotation=90)
		elif contQuantity == 'Stagnation Temperature ':
			T0 = self.units.conv_temp(self.state.T0[0:-1,1:-1])
			cont = panel.cax.contourf(cl*self.mesh.xxc[0:-1,1:-1], cl*self.mesh.yyc[0:-1,1:-1], \
							    		      	  T0, self.contGrad, cmap=self.cmOption)
			# colorbar settings
			ticks = np.linspace(round(np.min(T0),0), round(np.max(T0),0), 6)
			CB = panel.figure.colorbar(cont, ticks=ticks, \
												shrink=r, extend='both', ax=panel.cax)
			CB.set_label(contQuantity + ' (' + self.units.temp + ')', rotation=90)

		# set up contour labels
		if self.contQuantity != 'Velocity Quiver':
			if self.labeled:
				if len(cont.levels) > self.contGrad**(1/3):
					self.contourPanel.cax.clabel(cont, cont.levels[0:self.contGrad:int(self.contGrad*0.5/self.contGrad**(1/3))], fmt='%2.3f', colors='w', fontsize=8)
				else:
					self.contourPanel.cax.clabel(cont, fmt='%2.3f', colors='w', fontsize=8)

		# add airfoil if needed
		if self.gridChoice.StringSelection == 'NACA XXXX Airfoil' or self.gridChoice.StringSelection == 'Biconvex Airfoil':
			panel.cax.contourf(cl*self.mesh.xxc[self.domain.obj_i:self.domain.obj_f,self.domain.wallL:self.domain.wallU], \
							   cl*self.mesh.yyc[self.domain.obj_i:self.domain.obj_f,self.domain.wallL:self.domain.wallU], \
							    		      	self.state.Mach[self.domain.obj_i:self.domain.obj_f,self.domain.wallL:self.domain.wallU], self.contGrad, colors = 'gray')

		# plot settings
		if self.topwall_out.IsChecked():
			panel.cax.set(xlim=[np.min(self.mesh.xxc[1:-1,1:-1]) * cl, np.max(self.mesh.xxc[1:-1,1:-1]) * cl], \
					  	  ylim=[np.min(self.mesh.yyc[1:-1,1:-1]) * cl, np.max(self.mesh.yyc[1:-1,1:-1]) * cl])
		else:
			panel.cax.set(xlim=[np.min(self.mesh.xxc[1:-1,1:-1]) * cl, np.max(self.mesh.xxc[1:-1,1:-1]) * cl], \
					  	  ylim=[np.min(self.mesh.yyc[1:-1,1:-2]) * cl, np.max(self.mesh.yyc[1:-1,1:-2]) * cl])

		panel.cax.set_aspect(self.axisOption, adjustable='box', anchor='C')

		panel.cax.set_xlabel('x-coordinate' + ' (' + self.units.length + ')')
		panel.cax.set_ylabel('y-coordinate' + ' (' + self.units.length + ')')
		panel.canvas = FigureCanvas(panel, -1, panel.figure)

	def call_resplot(self):

		import numpy as np
		import matplotlib.pyplot as plt
		from matplotlib import cm
		import matplotlib as mpl
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

		# residual plotting
		self.iterPanel.figure.clf()
		self.iterPanel.iax = self.iterPanel.figure.gca()
		self.iterPanel.iax.set_position([0.14, 0.31, 0.68, 0.52]) 
		self.iterPanel.iax.plot(np.arange(1, len(self.state.res[0:self.state.n]), 1), self.state.res[1:self.state.n], linewidth=0.8)
		self.iterPanel.iax.set_xlabel('Iterations')
		self.iterPanel.iax.set_ylabel('Residual') 
		self.iterPanel.iax.get_lines()[0].set_color("black")
		self.iterPanel.iax.get_lines()[1].set_color("blue")
		self.iterPanel.iax.get_lines()[2].set_color("green")
		self.iterPanel.iax.get_lines()[3].set_color("red")
		self.iterPanel.iax.legend([r"$\dot{m}$", 'u', 'v', r"$h_{t}$"], loc='center left', bbox_to_anchor=(1.025, 0.5), framealpha=0.0)
		self.iterPanel.canvas = FigureCanvas(self.iterPanel, -1, self.iterPanel.figure)


	# menubar events
	def cont_change( self, event ):
		if self.mach.IsChecked():
			self.contQuantity = 'Mach'
		elif self.velocity.IsChecked():
			self.contQuantity = 'Velocity'
		elif self.quiver.IsChecked():
			self.contQuantity = 'Velocity Quiver'
		elif self.rho.IsChecked():
			self.contQuantity = 'Density'
		elif self.pressure.IsChecked():
			self.contQuantity = 'Pressure'
		elif self.stagp.IsChecked():
			self.contQuantity = 'Stagnation Pressure'
		elif self.temp.IsChecked():
			self.contQuantity = 'Temperature'
		elif self.stagtemp.IsChecked():
			self.contQuantity = 'Stagnation Temperature'

		if hasattr(self, 'state'):
			self.call_contplot(self.contourPanel, 1, 1)
		event.Skip()

	def cm_change( self, event ):
		from matplotlib import cm
		if self.jet.IsChecked():
			self.cmOption = cm.jet
		elif self.magma.IsChecked():
			self.cmOption = cm.magma
		elif self.gray.IsChecked():
			self.cmOption = cm.gray
		elif self.viridis.IsChecked():
			self.cmOption = cm.viridis
		elif self.coolwarm.IsChecked():
			self.cmOption = cm.coolwarm
		elif self.seismic.IsChecked():
			self.cmOption = cm.seismic

		if hasattr(self, 'state'):
			self.call_contplot(self.contourPanel, 1, 1)
		event.Skip()

	def unit_change( self, event ):
		class metric1:
			mass = 'kg'
			def conv_mass(m):
				conv = m
				return conv
			length = 'm'
			def conv_length(l):
				conv = l
				return conv
			time = 's'
			def conv_time(t):
				conv = t
				return conv
			temp = 'K'
			def conv_temp(T):
				conv = T
				return conv
			press = 'kPa'
			def conv_press(p):
				conv = p * 1000
				return conv
			energy = 'J'
			def conv_energy(e):
				conv = e
				return conv
		class metric2:
			mass = 'kg'
			def conv_mass(m):
				conv = m
				return conv
			length = 'm'
			def conv_length(l):
				conv = l
				return conv
			time = 's'
			def conv_time(t):
				conv = t
				return conv
			temp = '°C'
			def conv_temp(T):
				conv = T - 272.15
				return conv
			press = 'kPa'
			def conv_press(p):
				conv = p * 1000
				return conv
			energy = 'J'
			def conv_energy(e):
				conv = e
				return conv
		class imp1:
			mass = 'lbm'
			def conv_mass(m):
				conv = m * 2.20462
				return conv
			length = 'ft'
			def conv_length(l):
				conv = l * 3.28084
				return conv
			time = 's'
			def conv_time(t):
				conv = t
				return conv
			temp = '°F'
			def conv_temp(T):
				conv = (T - 272.15) * 9/5 + 32
				return conv
			press = 'psi'
			def conv_press(p):
				conv = p * 0.000145038
				return conv
			energy = 'ft-lbf'
			def conv_energy(e):
				conv = e * 0.737562
				return conv
		class imp2:
			mass = 'slug'
			def conv_mass(m):
				conv = m * 0.0685218
				return conv
			length = 'in'
			def conv_length(l):
				conv = l * 39.3701
				return conv
			time = 's'
			def conv_time(t):
				conv = t
				return conv
			temp = '°R'
			def conv_temp(T):
				conv = (T - 272.15) * 9/5 + 32 + 491.67
				return conv
			press = 'psi'
			def conv_press(p):
				conv = p * 0.000145038
				return conv
			energy = 'ft-lbf'
			def conv_energy(e):
				conv = e * 0.737562
				return conv

		if self.metric1.IsChecked():
			self.units = metric1
		elif self.metric2.IsChecked():
			self.units = metric2
		elif self.imperial1.IsChecked():
			self.units = imp1
		elif self.imperial2.IsChecked():
			self.units = imp2

		# update units on user input tables
		self.grid_change(wx.EVT_CHOICE)

		self.parameterGrid.SetRowLabelValue( 0, u"Inlet Mach #" )
		self.parameterGrid.SetRowLabelValue( 1, u"Inlet Pres. (" + self.units.press + ')' )
		self.parameterGrid.SetRowLabelValue( 2, u"Inlet Temp. (" + self.units.temp + ')' )

		if hasattr(self, 'state'):
			self.call_contplot(self.contourPanel, 1, 1)

	def axis_change( self, event ):
		if self.equal.IsChecked():
			self.axisOption = 'equal'
		elif self.tight.IsChecked():
			self.axisOption = 'tight'
		elif self.auto.IsChecked():
			self.axisOption = 'auto'
		if hasattr(self, 'state'):
			self.call_contplot(self.contourPanel, 1, 1)
		event.Skip()

	def contlevel_change( self, event ):
		if self.coarse.IsChecked():
			self.contGrad = 8
		elif self.medium.IsChecked():
			self.contGrad = 64
		elif self.fine.IsChecked():
			self.contGrad = 512

		if hasattr(self, 'state'):
			self.call_contplot(self.contourPanel, 1, 1)
		event.Skip()

	def label_change( self, event ):
		if self.labeled == False:
			self.labeled = True
		else:
			self.labeled = False
		if hasattr(self, 'state'):
			self.call_contplot(self.contourPanel, 1, 1)
		event.Skip()

	def gradient_change( self, event ):
		if self.gradient == 'Gradient':
			self.gradient = ''
			wx.MenuBar.Enable(self.menuBar, 1, True)
			wx.MenuBar.Enable(self.menuBar, 2, True)
			wx.MenuBar.Enable(self.menuBar, 3, True)

			wx.MenuBar.Enable(self.menuBar, 6, True)
			#wx.MenuBar.Enable(self.menuBar, 7, True)
			wx.MenuBar.Enable(self.menuBar, 8, True)

		else:
			self.gradient = 'Gradient'
			wx.MenuBar.Enable(self.menuBar, 1, False)
			wx.MenuBar.Enable(self.menuBar, 2, False)
			wx.MenuBar.Enable(self.menuBar, 3, False)

			wx.MenuBar.Enable(self.menuBar, 6, False)
			#wx.MenuBar.Enable(self.menuBar, 7, False)
			wx.MenuBar.Enable(self.menuBar, 8, False)

		if hasattr(self, 'state'):
			self.call_contplot(self.contourPanel, 1, 1)
		event.Skip()

	def gas_change( self, event ):
		if self.air.IsChecked() == True:
			self.gasSelect = 'Air'
		elif self.C02.IsChecked() == True:
			self.gasSelect = 'Carbon Dioxide'
		elif self.H2.IsChecked() == True:
			self.gasSelect = 'Hydrogen'
		event.Skip()
	
	def thermalgas_change( self, event ):
		if self.thermoModel == 'tpg':
			self.thermoModel = 'cpg'
		else: 
			self.thermoModel = 'tpg'
		event.Skip()

	def botwall_thermal_change( self, event ):
		self.faceselect = 'bot'
		self.bot_thermal_window = thermalWindow(parent=self)
		self.bot_thermal_window.Show()
		event.Skip()

	def topwall_thermal_change( self, event ):
		self.faceselect = 'top'
		self.top_thermal_window = thermalWindow(parent=self)
		self.top_thermal_window.Show()
		event.Skip()

	def topwall_change( self, event ):
		if self.topwall_invisc.IsChecked() or self.topwall_visc.IsChecked():
			self.topwall_adiabatic.Enable(True)
			self.topwall_isothermal.Enable(True)
			self.topwall_fixed.Enable(True)
		else:
			self.topwall_adiabatic.Enable(False)
			self.topwall_isothermal.Enable(False)
			self.topwall_fixed.Enable(False)
		event.Skip()

	def grid_change( self, event ):

		if self.gridChoice.StringSelection == 'Wedge' or self.gridChoice.StringSelection == 'Corner':
			self.domainGrid.ShowRow( 1 )
			self.domainGrid.ShowRow( 3 )
			self.domainGrid.ShowRow( 4 )
			#self.domainGrid.HideRow( 7 )

			self.domainGrid.SetRowLabelValue( 0, u"Length (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 1, u"Height (" + self.units.length + ')')
			self.domainGrid.SetRowLabelValue( 2, u"Wedge Start (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 3, u"Wedge End (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 4, u"Wedge Angle (°)" )
			self.domainGrid.SetRowLabelValue( 5, u"Horizontal Cells" )
			self.domainGrid.SetRowLabelValue( 6, u"Vertical Cells" )
		elif self.gridChoice.StringSelection == 'Cylinder':
			self.domainGrid.HideRow( 1 )
			self.domainGrid.HideRow( 3 )
			self.domainGrid.HideRow( 4 )
			#self.domainGrid.HideRow( 7 )

			self.domainGrid.SetRowLabelValue( 0, u"Domain Diam. (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 2, u"Cylinder Diam. (" + self.units.length + ')' )

			self.domainGrid.SetRowLabelValue( 5, u"Radial Cells" )
			self.domainGrid.SetRowLabelValue( 6, u"Tangential Cells" )

		elif self.gridChoice.StringSelection == "NACA XXXX Airfoil":
			self.domainGrid.ShowRow( 1 )
			self.domainGrid.ShowRow( 3 )
			self.domainGrid.ShowRow( 4 )
			#self.domainGrid.ShowRow( 7 )

			self.domainGrid.SetRowLabelValue( 0, u"Length (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 1, u"Height (" + self.units.length + ')')
			self.domainGrid.SetRowLabelValue( 2, u"Airfoil Start (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 3, u"Airfoil End (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 4, u"NACA XXXX" )
			self.domainGrid.SetRowLabelValue( 5, u"Horizontal Cells" )
			self.domainGrid.SetRowLabelValue( 6, u"Vertical Cells" )
			#self.domainGrid.SetRowLabelValue( 7, u"Angle of Attack (°)" )

		elif self.gridChoice.StringSelection == 'Biconvex Airfoil':
			self.domainGrid.ShowRow( 1 )
			self.domainGrid.ShowRow( 3 )
			self.domainGrid.ShowRow( 4 )
			#self.domainGrid.ShowRow( 7 )

			self.domainGrid.SetRowLabelValue( 0, u"Length (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 1, u"Height (" + self.units.length + ')')
			self.domainGrid.SetRowLabelValue( 2, u"Airfoil Start (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 3, u"Airfoil End (" + self.units.length + ')' )
			self.domainGrid.SetRowLabelValue( 4, u"Thickness (" + self.units.length + ')')
			self.domainGrid.SetRowLabelValue( 5, u"Horizontal Cells" )
			self.domainGrid.SetRowLabelValue( 6, u"Vertical Cells" )
			#self.domainGrid.SetRowLabelValue( 7, u"Angle of Attack (°)" )

	# open contour plot in new window
	def expandWindow( self, event ):
		self.new = NewWindow(parent=None)
		x = self.new.screenInX
		y = self.new.screenInY

		scx = x/5.6 * 0.9
		scy = y/4.0 * 0.9
		#scale = min(scx, scy)

		self.call_contplot(self.new.contourPanel, scx, scy)
		self.new.Show()
		event.Skip()

	# open informational window for gases
	def infoWindow( self, event ):
		self.new = tableWindow(  parent=self )
		self.new.Show()


class RedirectText:
	def __init__(self,aWxTextCtrl):
		self.out=aWxTextCtrl

	def write(self,string):
		self.out.WriteText(string)

		# redir=RedirectText(self.consolePanel.text)
		# sys.stdout=redir


class NewWindow( wx.Frame ):
	def __init__(self, parent):
		import matplotlib.pyplot as plt
		#from matplotlib.backends.backend_gtk3 import (NavigationToolbar2GTK3 as NavigationToolbar)
		import numpy as np
		# import gi
		# gi.require_version("Gtk", "3.0")
		# from gi.repository import Gtk

		screenSize = wx.DisplaySize()
		screenMM = wx.DisplaySizeMM()
		self.screenInX = float(screenMM[0]) * 0.0393701
		self.screenInY = float(screenMM[1]) * 0.0393701

		wx.Frame.__init__( self, parent, title = 'Fullscreen Contour Plot',\
						   size = wx.Size( int(screenSize[0]*0.96), int(screenSize[1]*0.96) ), style=wx.DEFAULT_FRAME_STYLE )

		self.SetBackgroundColour( wx.Colour( 256, 256, 256 ) )

		self.contourPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.contourPanel.SetBackgroundColour( wx.Colour( 256, 256, 256 ) )

		#self.contourPanel.figure = plt.figure( dpi=100, figsize=(9, 9/1.4473))
		self.contourPanel.figure = plt.figure( dpi=100, figsize=(self.screenInX, self.screenInY))
		self.contourPanel.cax = self.contourPanel.figure.gca()
		self.contourPanel.cax.set_facecolor((0.4, 0.4, 0.4))
		self.contourPanel.cax.set_position([0.15, 0.1, 0.8, 0.72])


class tableWindow(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__( self, parent, title = parent.gasSelect + ' Properties',\
						size = wx.Size( 300, 294 ), style=wx.DEFAULT_FRAME_STYLE )
		import gui1
		import python.finite_volume.gasdata as gasdata
		import numpy as np
		import matplotlib.pyplot as plt
		from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

		sizer = wx.BoxSizer(wx.VERTICAL)

		# Gas information grid
		self.gasGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gasGrid.CreateGrid( 5, 1 )
		self.gasGrid.SetRowLabelSize( 190 )
		self.gasGrid.SetColLabelSize( 0 )
		self.gasGrid.SetRowLabelValue( 0, u"Temperature " + '(' + parent.units.temp + ')' )
		self.gasGrid.SetRowLabelValue( 1, u"Specific Heat Ratio" )
		self.gasGrid.SetRowLabelValue( 2, u"Cp " + '(' + parent.units.energy + '/' + parent.units.mass + parent.units.temp + ')')
		self.gasGrid.SetRowLabelValue( 3, u"Cv " + '(' + parent.units.energy + '/' + parent.units.mass + parent.units.temp + ')' )
		self.gasGrid.SetRowLabelValue( 4, u"R " + '(' + parent.units.energy + '/' + parent.units.mass + parent.units.temp + ')')

		self.gasPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.gasPanel.SetBackgroundColour( wx.Colour( 256, 256, 256 ) )

		#sizer.Add( self.gasPanel, 0, wx.CENTER )

		self.gasGrid.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.gasdata_change )
		self.temp = 300
		self.units = parent.units

		if parent.thermoModel == 'cpg':
			if parent.gasSelect == 'Air':
				self.gas = gasdata.air_cpg
			elif parent.gasSelect == 'Carbon Dioxide':
				self.gas = gasdata.C02_cpg
			elif parent.gasSelect == 'Hydrogen':
				self.gas = gasdata.H2_cpg
		elif parent.thermoModel == 'tpg':
			if parent.gasSelect == 'Air':
				self.gas = gasdata.air_tpg
			elif parent.gasSelect == 'Carbon Dioxide':
				self.gas = gasdata.C02_tpg
			elif parent.gasSelect == 'Hydrogen':
				self.gas = gasdata.H2_tpg

		T = np.linspace(0, 4000, 100)

		if self.units.temp == '°C':
			self.gasGrid.SetCellValue( 0, 0, '0')
			T_plot = np.linspace(-273, 4000-273, 100)
		elif self.units.temp == '°F':
			self.gasGrid.SetCellValue( 0, 0, '32')
			T_plot = np.linspace(-459.67, 6740.33, 100)
		elif self.units.temp == '°R':
			self.gasGrid.SetCellValue( 0, 0, '459.67')
			T_plot = T * (9/5)
		else:
			self.gasGrid.SetCellValue( 0, 0, '273.15')
			T_plot = T

		self.gasdata_change( wx.grid.EVT_GRID_CELL_CHANGED )

		self.gasGrid.EnableEditing( True )
		self.gasGrid.EnableGridLines( True )
		self.gasGrid.EnableDragGridSize( False )
		self.gasGrid.SetMargins( 0, 0 )

		self.gasGrid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		sizer.Add( self.gasGrid, 0, wx.EXPAND | wx.ALL, 0 )
		self.gasPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		sizer.Add( self.gasPanel, 1, wx.EXPAND | wx.ALL, 0 )
		
		self.SetSizer( sizer )
		self.Layout()
		
		self.Centre( wx.BOTH )

		self.gasPanel.fig = plt.figure( dpi=100, figsize=(2.99, 1.6), facecolor=(1, 1, 1) )
		self.gasPanel.ax = self.gasPanel.fig.gca()

		self.gasPanel.ax.plot( T_plot, self.gas.Cp_fn(self.gas.gamma_p, self.gas.Cp_p, self.gas.theta, T) \
									 / self.gas.Cv_fn(self.gas.gamma_p, self.gas.Cv_p, self.gas.theta, T), color='k' )

		self.gasPanel.ax.set_xlabel('Temperature' + ' (' + self.units.temp + ')', fontsize=8)
		self.gasPanel.ax.tick_params( axis='x', labelsize=8 )
		self.gasPanel.ax.set_ylabel('$\gamma$', fontsize=8)
		self.gasPanel.ax.tick_params( axis='y', labelsize=8 )
		self.gasPanel.ax.set_position([0.2, 0.27, 0.7, 0.66], which='both')
		self.gasPanel.ax.set_aspect('auto', adjustable='box', anchor='C')
		self.gasPanel.canvas = FigureCanvas(self.gasPanel, -1, self.gasPanel.fig)

	def gasdata_change(self, event):
		gas = self.gas
		if self.units.temp == '°C':
			temp = float(self.gasGrid.GetCellValue(0, 0)) + 273.15
			conv = 1 / (self.units.conv_energy(1) / (self.units.conv_mass(1)*(self.units.conv_temp(0)+273.15)))
		elif self.units.temp == '°F':
			temp = (float(self.gasGrid.GetCellValue(0, 0))-32)*(5/9) + 273.15
			conv = 1 / (self.units.conv_energy(1) / self.units.conv_mass(1))
		else:
			temp = float(self.gasGrid.GetCellValue(0, 0))
			conv = 1 / (self.units.conv_energy(1) / (self.units.conv_mass(1)*self.units.conv_temp(1)))

		input_temp = float(self.gasGrid.GetCellValue(0, 0))

		self.gasGrid.SetCellValue( 0, 0, str(input_temp))
		self.gasGrid.SetCellValue( 1, 0, str( round( gas.Cp_fn(gas.gamma_p, gas.Cp_p, gas.theta, temp) \
													/ gas.Cv_fn(gas.gamma_p, gas.Cv_p, gas.theta, temp), 4) ) )
		self.gasGrid.SetCellValue( 2, 0, str( conv*round( gas.Cp_fn(gas.gamma_p, gas.Cp_p, gas.theta, temp), 2 ) ) )
		self.gasGrid.SetCellValue( 3, 0, str( conv*round( gas.Cv_fn(gas.gamma_p, gas.Cv_p, gas.theta, temp), 2 ) ) )
		self.gasGrid.SetCellValue( 4, 0, str( conv*round( gas.Cp_fn(gas.gamma_p, gas.Cp_p, gas.theta, temp) - \
															gas.Cv_fn(gas.gamma_p, gas.Cv_p, gas.theta, temp), 2) ) )


class thermalWindow(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__( self, parent, title = 'Wall' + ' Properties',\
						size = wx.Size( 236, 58 ), style=wx.DEFAULT_FRAME_STYLE )

		self.wallGrid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wallGrid.CreateGrid( 1, 1 )
		self.wallGrid.SetRowLabelSize( 140 )
		self.wallGrid.SetColLabelSize( 0 )

		self.wallGrid.SetRowLabelValue( 0, u"Wall Temperature " + '(' + parent.units.temp + ')' )

		if parent.faceselect == 'bot' and hasattr(parent, 'bot_thermal_window'):
			self.wallGrid.SetCellValue( 0, 0, str(parent.bot_thermal_window.walltemp))
		elif parent.faceselect == 'top' and hasattr(parent, 'top_thermal_window'):
			self.wallGrid.SetCellValue( 0, 0, str(parent.top_thermal_window.walltemp))
		else:
			self.wallGrid.SetCellValue( 0, 0, '300')

		self.walltemp = self.wallGrid.GetCellValue( 0, 0 )
		self.wallGrid.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.wall_change )

	def wall_change( self, event ):
		self.walltemp = self.wallGrid.GetCellValue( 0, 0 )

