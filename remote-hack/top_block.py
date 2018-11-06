#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Nov  5 01:26:33 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from datetime import datetime
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.prefix = prefix = "/root/Desktop/cse825/Key Fob/2010 Focus/demoreal/"
        self.filename = filename = "11-04-2015.10:08:05.dat"
        self.tuner_freq = tuner_freq = 314e6
        self.thabaseband = thabaseband = 314.95e6
        self.target_freq = target_freq = 433.92e6
        self.samp_rate = samp_rate = 2e6
        self.recfilepath = recfilepath = prefix + datetime.now().strftime("%m-%d-%Y.%H:%M:%S") + ".dat"
        self.multcosfreq = multcosfreq = 975e3
        self.cosfreq = cosfreq = 314.95e6
        self.TxFilePath = TxFilePath = prefix + filename

        ##################################################
        # Blocks
        ##################################################
        self._target_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	value=self.target_freq,
        	callback=self.set_target_freq,
        	label="target_freq",
        	converter=forms.float_converter(),
        )
        self.Add(self._target_freq_text_box)
        self.wxgui_fftsink2_2 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=433.92e6,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title="FFT Plot nonmuls",
        	peak_hold=True,
        )
        self.Add(self.wxgui_fftsink2_2.win)
        _tuner_freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._tuner_freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_tuner_freq_sizer,
        	value=self.tuner_freq,
        	callback=self.set_tuner_freq,
        	label="tuner_freq",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._tuner_freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_tuner_freq_sizer,
        	value=self.tuner_freq,
        	callback=self.set_tuner_freq,
        	minimum=300e6,
        	maximum=330e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_tuner_freq_sizer)
        _thabaseband_sizer = wx.BoxSizer(wx.VERTICAL)
        self._thabaseband_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_thabaseband_sizer,
        	value=self.thabaseband,
        	callback=self.set_thabaseband,
        	label='thabaseband',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._thabaseband_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_thabaseband_sizer,
        	value=self.thabaseband,
        	callback=self.set_thabaseband,
        	minimum=310e6,
        	maximum=320e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_thabaseband_sizer)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(target_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(5, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        _multcosfreq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._multcosfreq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_multcosfreq_sizer,
        	value=self.multcosfreq,
        	callback=self.set_multcosfreq,
        	label='multcosfreq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._multcosfreq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_multcosfreq_sizer,
        	value=self.multcosfreq,
        	callback=self.set_multcosfreq,
        	minimum=0,
        	maximum=1e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_multcosfreq_sizer)
        _cosfreq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cosfreq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cosfreq_sizer,
        	value=self.cosfreq,
        	callback=self.set_cosfreq,
        	label='cosfreq',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cosfreq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cosfreq_sizer,
        	value=self.cosfreq,
        	callback=self.set_cosfreq,
        	minimum=312e6,
        	maximum=316e6,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_cosfreq_sizer)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/home/mike/GitHub/sayboltm/HackRFOne/remote-hack/off2_10-05-2018.00:38:49.dat", False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.osmosdr_sink_0, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.wxgui_fftsink2_2, 0))    

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix
        self.set_TxFilePath(self.prefix + self.filename)
        self.set_recfilepath(self.prefix + datetime.now().strftime("%m-%d-%Y.%H:%M:%S") + ".dat")

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.set_TxFilePath(self.prefix + self.filename)

    def get_tuner_freq(self):
        return self.tuner_freq

    def set_tuner_freq(self, tuner_freq):
        self.tuner_freq = tuner_freq
        self._tuner_freq_slider.set_value(self.tuner_freq)
        self._tuner_freq_text_box.set_value(self.tuner_freq)

    def get_thabaseband(self):
        return self.thabaseband

    def set_thabaseband(self, thabaseband):
        self.thabaseband = thabaseband
        self._thabaseband_slider.set_value(self.thabaseband)
        self._thabaseband_text_box.set_value(self.thabaseband)

    def get_target_freq(self):
        return self.target_freq

    def set_target_freq(self, target_freq):
        self.target_freq = target_freq
        self._target_freq_text_box.set_value(self.target_freq)
        self.osmosdr_sink_0.set_center_freq(self.target_freq, 0)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.wxgui_fftsink2_2.set_sample_rate(self.samp_rate)

    def get_recfilepath(self):
        return self.recfilepath

    def set_recfilepath(self, recfilepath):
        self.recfilepath = recfilepath

    def get_multcosfreq(self):
        return self.multcosfreq

    def set_multcosfreq(self, multcosfreq):
        self.multcosfreq = multcosfreq
        self._multcosfreq_slider.set_value(self.multcosfreq)
        self._multcosfreq_text_box.set_value(self.multcosfreq)

    def get_cosfreq(self):
        return self.cosfreq

    def set_cosfreq(self, cosfreq):
        self.cosfreq = cosfreq
        self._cosfreq_slider.set_value(self.cosfreq)
        self._cosfreq_text_box.set_value(self.cosfreq)

    def get_TxFilePath(self):
        return self.TxFilePath

    def set_TxFilePath(self, TxFilePath):
        self.TxFilePath = TxFilePath


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
