# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 25 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"I want a...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Single Figure", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Multi-Figure Spread", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.openSingleFigWindow )
		self.m_button2.Bind( wx.EVT_BUTTON, self.openMultiFigWindow )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def openSingleFigWindow( self, event ):
		event.Skip()

	def openMultiFigWindow( self, event ):
		event.Skip()


###########################################################################
## Class singleFrame
###########################################################################

class singleFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,741 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.ra_label = wx.StaticText( self, wx.ID_ANY, u"RA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ra_label.Wrap( -1 )

		bSizer3.Add( self.ra_label, 0, wx.ALL, 5 )

		self.ra_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.ra_box, 0, wx.ALL, 5 )

		self.dec_label = wx.StaticText( self, wx.ID_ANY, u"Dec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dec_label.Wrap( -1 )

		bSizer3.Add( self.dec_label, 0, wx.ALL, 5 )

		self.dec_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.dec_box, 0, wx.ALL, 5 )

		self.lat_label = wx.StaticText( self, wx.ID_ANY, u"Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lat_label.Wrap( -1 )

		bSizer3.Add( self.lat_label, 0, wx.ALL, 5 )

		self.lat_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.lat_box, 0, wx.ALL, 5 )

		self.long_label = wx.StaticText( self, wx.ID_ANY, u"Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.long_label.Wrap( -1 )

		bSizer3.Add( self.long_label, 0, wx.ALL, 5 )

		self.long_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.long_box, 0, wx.ALL, 5 )

		self.elev_label = wx.StaticText( self, wx.ID_ANY, u"Elevation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.elev_label.Wrap( -1 )

		bSizer3.Add( self.elev_label, 0, wx.ALL, 5 )

		self.elev_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.elev_box, 0, wx.ALL, 5 )

		self.utc_label = wx.StaticText( self, wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.utc_label.Wrap( -1 )

		bSizer3.Add( self.utc_label, 0, wx.ALL, 5 )

		self.utc_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.utc_box, 0, wx.ALL, 5 )

		self.period_label = wx.StaticText( self, wx.ID_ANY, u"Period", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_label.Wrap( -1 )

		bSizer3.Add( self.period_label, 0, wx.ALL, 5 )

		self.period_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.period_box, 0, wx.ALL, 5 )

		self.HJD_label = wx.StaticText( self, wx.ID_ANY, u"Start HJD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.HJD_label.Wrap( -1 )

		bSizer3.Add( self.HJD_label, 0, wx.ALL, 5 )

		self.hjd_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.hjd_box, 0, wx.ALL, 5 )

		self.startDay_label = wx.StaticText( self, wx.ID_ANY, u"Start Date", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.startDay_label.Wrap( -1 )

		bSizer3.Add( self.startDay_label, 0, wx.ALL, 5 )

		self.initialPoint_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.initialPoint_box, 0, wx.ALL, 5 )

		self.single_submit_button = wx.Button( self, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.single_submit_button, 0, wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.single_submit_button.Bind( wx.EVT_BUTTON, self.getInfo )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def getInfo( self, event ):
		event.Skip()


###########################################################################
## Class testFrame2
###########################################################################

class testFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1271,391 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 8, 7, 0, 0 )

		self.tName_label = wx.StaticText( self, wx.ID_ANY, u"Target Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tName_label.Wrap( -1 )

		gSizer1.Add( self.tName_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.tName_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tName_box.SetToolTip( u"Name of target star" )

		gSizer1.Add( self.tName_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.date_label = wx.StaticText( self, wx.ID_ANY, u"Date of First Observation", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_label.Wrap( -1 )

		gSizer1.Add( self.date_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.startDate_box = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		self.startDate_box.SetToolTip( u"Date, centered on midnight, for which first figure will be generated" )

		gSizer1.Add( self.startDate_box, 0, wx.ALL, 5 )

		self.numFigs_label = wx.StaticText( self, wx.ID_ANY, u"Number of Figures", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.numFigs_label.Wrap( -1 )

		gSizer1.Add( self.numFigs_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		numDays_boxChoices = [ u"1", u"3", u"6", u"9", u"12", u"15", u"18", u"21", u"24", u"27", u"30" ]
		self.numDays_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, numDays_boxChoices, 0 )
		self.numDays_box.SetSelection( 0 )
		self.numDays_box.SetToolTip( u"Number of figures to generate" )

		gSizer1.Add( self.numDays_box, 0, wx.ALL, 5 )

		self.tCoords_label = wx.StaticText( self, wx.ID_ANY, u"RA, Dec", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tCoords_label.Wrap( -1 )

		gSizer1.Add( self.tCoords_label, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.ra_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ra_box.SetToolTip( u"Right Ascension" )

		gSizer1.Add( self.ra_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.dec_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.dec_box.SetToolTip( u"Declination" )

		gSizer1.Add( self.dec_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		RaDec_unit_boxChoices = [ u"Sexagesimal", u"Degrees" ]
		self.RaDec_unit_box = wx.RadioBox( self, wx.ID_ANY, u"RA, Dec in:", wx.DefaultPosition, wx.DefaultSize, RaDec_unit_boxChoices, 2, wx.RA_SPECIFY_COLS )
		self.RaDec_unit_box.SetSelection( 0 )
		gSizer1.Add( self.RaDec_unit_box, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.period_label = wx.StaticText( self, wx.ID_ANY, u"Period", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_label.Wrap( -1 )

		gSizer1.Add( self.period_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.period_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.period_box.SetToolTip( u"Enter period of target star, in days" )

		gSizer1.Add( self.period_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.hjd_label = wx.StaticText( self, wx.ID_ANY, u"Past HJD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hjd_label.Wrap( -1 )

		gSizer1.Add( self.hjd_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.initialHJD_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.initialHJD_box.SetToolTip( u"Enter most recent HJD of point on light curve to be observed" )

		gSizer1.Add( self.initialHJD_box, 0, wx.ALL, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.obs_label = wx.StaticText( self, wx.ID_ANY, u"Observatory", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.obs_label.Wrap( -1 )

		gSizer1.Add( self.obs_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		obs_boxChoices = [ u"Custom", u"RIT Observatory", u"WIYN 0.9m at KPNO" ]
		self.obs_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, obs_boxChoices, 0 )
		self.obs_box.SetSelection( 0 )
		self.obs_box.SetToolTip( u"Select an observatory, OR select 'custom' and enter observatory latitude, longitude, and elevation below" )

		gSizer1.Add( self.obs_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"OR, Choose 'Custom' and Enter Coordinates Below", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		gSizer1.Add( self.m_staticText24, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.lat_long_label = wx.StaticText( self, wx.ID_ANY, u"Latitude and Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lat_long_label.Wrap( -1 )

		gSizer1.Add( self.lat_long_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.lat_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lat_box.SetToolTip( u"Latitude of observing site" )

		gSizer1.Add( self.lat_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		NS_boxChoices = [ u"N", u"S" ]
		self.NS_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, NS_boxChoices, 0 )
		self.NS_box.SetSelection( 0 )
		gSizer1.Add( self.NS_box, 0, wx.ALL, 5 )

		self.long_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.long_box.SetToolTip( u"Longitude of observing site" )

		gSizer1.Add( self.long_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		EW_boxChoices = [ u"E", u"W" ]
		self.EW_box = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, EW_boxChoices, 0 )
		self.EW_box.SetSelection( 0 )
		gSizer1.Add( self.EW_box, 0, wx.ALL, 5 )

		self.elev_label = wx.StaticText( self, wx.ID_ANY, u"Elevation (m)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.elev_label.Wrap( -1 )

		gSizer1.Add( self.elev_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.elev_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.elev_box.SetToolTip( u"Elevation of observing site" )

		gSizer1.Add( self.elev_box, 0, wx.ALL, 5 )

		self.utc_label = wx.StaticText( self, wx.ID_ANY, u"UTC Offset", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.utc_label.Wrap( -1 )

		gSizer1.Add( self.utc_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.utc_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.utc_box.SetToolTip( u"UTC offset for date and location of observations" )

		gSizer1.Add( self.utc_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.altLim_label = wx.StaticText( self, wx.ID_ANY, u"Limiting Altitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.altLim_label.Wrap( -1 )

		gSizer1.Add( self.altLim_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.altLim_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.altLim_box.SetToolTip( u"Minimum observable altitude" )

		gSizer1.Add( self.altLim_box, 0, wx.ALL, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.saveFile_check = wx.CheckBox( self, wx.ID_ANY, u"Save Data File", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.saveFile_check, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.saveFile_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.saveFile_box.SetToolTip( u"Filename for data file, if desired" )

		gSizer1.Add( self.saveFile_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.saveFig_check = wx.CheckBox( self, wx.ID_ANY, u"Save Figure", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.saveFig_check, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.saveFig_box = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.saveFig_box.SetToolTip( u"Filename for figure, if desired" )

		gSizer1.Add( self.saveFig_box, 0, wx.ALL, 5 )

		self.filePath_label = wx.StaticText( self, wx.ID_ANY, u"Save Path", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.filePath_label.Wrap( -1 )

		gSizer1.Add( self.filePath_label, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.filePath_box = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		self.filePath_box.SetToolTip( u"path for saving files and images, if desired" )

		gSizer1.Add( self.filePath_box, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.submit_button = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.submit_button.SetToolTip( u"Click to create figures" )

		gSizer1.Add( self.submit_button, 0, wx.ALL, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		gSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.obs_box.Bind( wx.EVT_CHOICE, self.setObsCoords )
		self.lat_box.Bind( wx.EVT_TEXT, self.setObsCustom )
		self.NS_box.Bind( wx.EVT_CHOICE, self.setObsCustom )
		self.long_box.Bind( wx.EVT_TEXT, self.setObsCustom )
		self.EW_box.Bind( wx.EVT_CHOICE, self.setObsCustom )
		self.elev_box.Bind( wx.EVT_TEXT, self.setObsCustom )
		self.submit_button.Bind( wx.EVT_BUTTON, self.getInfo )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def setObsCoords( self, event ):
		event.Skip()

	def setObsCustom( self, event ):
		event.Skip()





	def getInfo( self, event ):
		event.Skip()


###########################################################################
## Class figFrame
###########################################################################

class figFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1050,753 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"temp.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_bitmap1, 0, wx.ALL, 5 )


		self.SetSizer( gSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


