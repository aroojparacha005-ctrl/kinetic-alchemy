import numpy as np
from scipy.io.wavfile import write
import streamlit as st
from pathlib import Path

class SoundGenerator:
    """Generate audio effects"""
    
    def __init__(self, sr=44100):
        self.sr = sr
        self.sound_dir = Path("assets/sounds")
        self.sound_dir.mkdir(exist_ok=True, parents=True)
    
    def _write_audio(self, filename, audio):
        write(self.sound_dir / filename, self.sr, audio.astype(np.int16))
    
    def success_chime(self):
        """800Hz sparkle"""
        t = np.linspace(0, 0.5, int(self.sr * 0.5), False)
        audio = np.sin(2*np.pi*800*t)*0.4 + np.sin(2*np.pi*1200*t)*0.2 + np.sin(2*np.pi*1600*t)*0.15
        audio *= np.exp(-2*t)
        self._write_audio("success.wav", audio/np.max(np.abs(audio))*32767)
    
    def failure_buzz(self):
        """150Hz descending"""
        t = np.linspace(0, 0.4, int(self.sr * 0.4), False)
        freq = 150 - 50*t/0.4
        audio = np.sin(2*np.pi*freq*t)*0.5 * np.exp(-8*t)
        self._write_audio("failure.wav", audio/np.max(np.abs(audio))*32767)
    
    def level_up_ding(self):
        """1000Hz ding"""
        t = np.linspace(0, 0.6, int(self.sr * 0.6), False)
        audio = (np.sin(2*np.pi*1000*t)*0.5 + np.sin(2*np.pi*800*t)*0.3) * np.exp(-3*t)
        self._write_audio("levelup.wav", audio/np.max(np.abs(audio))*32767)
    
    def bagel_crunch(self):
        """3500Hz crunch"""
        t = np.linspace(0, 0.3, int(self.sr * 0.3), False)
        noise = np.random.normal(0, 0.3, len(t))
        audio = np.sin(2*np.pi*3500*t)*0.2 + noise*0.3
        envelope = np.ones_like(t)
        envelope[:int(0.05*self.sr)] = np.linspace(0, 1, int(0.05*self.sr))
        envelope[int(0.05*self.sr):] *= np.exp(-8*(t[int(0.05*self.sr):] - t[int(0.05*self.sr)]))
        self._write_audio("bagel.wav", audio*envelope/np.max(np.abs(audio*envelope))*32767*0.8)
    
    def distress_alarm(self):
        """500Hz descending alarm"""
        t = np.linspace(0, 0.8, int(self.sr * 0.8), False)
        freq = 500 - 300*t/0.8
        pulse = (np.sin(2*np.pi*4*t)+1)/2
        audio = np.sin(2*np.pi*freq*t)*0.6*pulse
        envelope = np.ones_like(t)
        envelope[-int(self.sr*0.2):] *= np.exp(-10*(t[-int(self.sr*0.2):] - t[-int(self.sr*0.2)]))
        self._write_audio("distress.wav", audio*envelope/np.max(np.abs(audio*envelope))*32767)
    
    def ambient_music(self):
        """30-second looping track"""
        t = np.linspace(0, 30, int(self.sr * 30), False)
        bass = np.sin(2*np.pi*130.81*t)*0.3
        mid = np.sin(2*np.pi*164.81*t)*0.25
        high = np.sin(2*np.pi*196*t)*0.2
        melody_freq = [261.63, 329.63, 392, 261.63, 293.66, 349.23, 392, 261.63]
        melody = np.zeros_like(t)
        samp_per_note = int(self.sr / (len(melody_freq) / 30))
        for i, freq in enumerate(melody_freq):
            start, end = i*samp_per_note, (i+1)*samp_per_note
            if end < len(t):
                melody[start:end] += np.sin(2*np.pi*freq*t[start:end])*0.15
        audio = (bass + mid + high + melody)*0.4
        envelope = np.ones_like(t)
        envelope[:self.sr] = np.linspace(0, 1, self.sr)
        envelope[-int(self.sr*2):] *= np.exp(-2*(t[-int(self.sr*2):] - t[-int(self.sr*2)]))
        self._write_audio("ambient.wav", audio*envelope/np.max(np.abs(audio*envelope))*32767*0.7)
    
    def generate_all(self):
        self.success_chime()
        self.failure_buzz()
        self.level_up_ding()
        self.bagel_crunch()
        self.distress_alarm()
        self.ambient_music()
        return True

class SoundPlayer:
    def __init__(self, sound_dir="assets/sounds"):
        self.sound_dir = Path(sound_dir)
    
    def play(self, sound_name):
        path = self.sound_dir / f"{sound_name}.wav"
        if path.exists():
            st.audio(str(path), format="audio/wav", autoplay=True)
