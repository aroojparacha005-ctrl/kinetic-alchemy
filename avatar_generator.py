import streamlit as st
import base64

class AvatarGenerator:
    """SVG-based 2D avatars showing nutrient deficiency symptoms"""
    
    def __init__(self):
        self.avatars = {
            "healthy": self._healthy(),
            "vitamin_a": self._vitamin_a(),
            "vitamin_d": self._vitamin_d(),
            "iron": self._iron(),
            "b12": self._b12(),
            "zinc": self._zinc(),
            "vitamin_c_toxicity": self._vitamin_c_toxicity(),
            "iodine": self._iodine(),
        }
    
    def _healthy(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <defs>
                <radialGradient id="glow"><stop offset="0%" style="stop-color:#FFD700"/><stop offset="100%" style="stop-color:#FFA500" stop-opacity="0.3"/></radialGradient>
                <filter id="blur"><feGaussianBlur stdDeviation="3"/></filter>
            </defs>
            <circle cx="200" cy="250" r="180" fill="url(#glow)" opacity="0.6" filter="url(#blur)"/>
            <circle cx="200" cy="120" r="70" fill="#F4C69C" stroke="#00D4FF" stroke-width="2"/>
            <circle cx="175" cy="100" r="12" fill="white"/><circle cx="175" cy="100" r="8" fill="#1E90FF"/><circle cx="175" cy="100" r="4" fill="black"/>
            <circle cx="225" cy="100" r="12" fill="white"/><circle cx="225" cy="100" r="8" fill="#1E90FF"/><circle cx="225" cy="100" r="4" fill="black"/>
            <path d="M 180 140 Q 200 155 220 140" stroke="#00D4FF" stroke-width="3" fill="none" stroke-linecap="round"/>
            <ellipse cx="200" cy="120" rx="65" ry="65" fill="none" stroke="#90EE90" stroke-width="1" opacity="0.8"/>
            <rect x="140" y="200" width="120" height="100" rx="20" fill="#87CEEB" stroke="#00D4FF" stroke-width="2"/>
            <line x1="140" y1="220" x2="80" y2="150" stroke="#F4C69C" stroke-width="15" stroke-linecap="round"/>
            <line x1="260" y1="220" x2="320" y2="150" stroke="#F4C69C" stroke-width="15" stroke-linecap="round"/>
            <line x1="160" y1="300" x2="160" y2="400" stroke="#8B4513" stroke-width="12" stroke-linecap="round"/>
            <line x1="240" y1="300" x2="240" y2="400" stroke="#8B4513" stroke-width="12" stroke-linecap="round"/>
            <ellipse cx="160" cy="410" rx="20" ry="10" fill="#654321"/><ellipse cx="240" cy="410" rx="20" ry="10" fill="#654321"/>
            <circle cx="120" cy="100" r="3" fill="#FFD700" opacity="0.8"/><circle cx="280" cy="100" r="3" fill="#FFD700" opacity="0.8"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="15" fill="#FFD700" stroke="#00D4FF" stroke-width="2"/><text x="-5" y="5" font-size="20" fill="white">👍</text></g>
        </svg>'''
    
    def _vitamin_a(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <rect width="400" height="500" fill="#2F2F2F" opacity="0.1"/>
            <circle cx="200" cy="120" r="70" fill="#D4A574" stroke="#808080" stroke-width="2" opacity="0.8"/>
            <ellipse cx="160" cy="90" rx="15" ry="20" fill="#8B7355" opacity="0.7"/><ellipse cx="240" cy="95" rx="12" ry="18" fill="#8B7355" opacity="0.7"/>
            <circle cx="175" cy="100" r="12" fill="#E8E8E8" opacity="0.6"/><circle cx="175" cy="100" r="8" fill="#A9A9A9" opacity="0.7"/><circle cx="175" cy="100" r="4" fill="#555555" opacity="0.8"/>
            <circle cx="225" cy="100" r="12" fill="#E8E8E8" opacity="0.6"/><circle cx="225" cy="100" r="8" fill="#A9A9A9" opacity="0.7"/><circle cx="225" cy="100" r="4" fill="#555555" opacity="0.8"/>
            <path d="M 180 140 Q 200 135 220 140" stroke="#696969" stroke-width="2" fill="none" stroke-linecap="round"/>
            <rect x="140" y="200" width="120" height="100" rx="20" fill="#B0C4DE" stroke="#696969" stroke-width="2" opacity="0.8"/>
            <line x1="140" y1="230" x2="70" y2="280" stroke="#D4A574" stroke-width="15" stroke-linecap="round" opacity="0.8"/>
            <line x1="260" y1="230" x2="330" y2="280" stroke="#D4A574" stroke-width="15" stroke-linecap="round" opacity="0.8"/>
            <line x1="160" y1="300" x2="160" y2="400" stroke="#654321" stroke-width="12" stroke-linecap="round" opacity="0.8"/>
            <line x1="240" y1="300" x2="245" y2="405" stroke="#654321" stroke-width="12" stroke-linecap="round" opacity="0.8"/>
            <ellipse cx="160" cy="410" rx="20" ry="10" fill="#654321" opacity="0.8"/><ellipse cx="245" cy="415" rx="20" ry="10" fill="#654321" opacity="0.8"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="15" fill="#FF6347" stroke="#FF0000" stroke-width="2"/><text x="-4" y="6" font-size="20" fill="white">⚠</text></g>
            <text x="200" y="480" text-anchor="middle" font-size="11" fill="#FF6347" font-weight="bold">Dull Eyes • Hyperkeratosis</text>
        </svg>'''
    
    def _vitamin_d(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <circle cx="200" cy="120" r="70" fill="#E8D4C0" stroke="#C0C0C0" stroke-width="2" opacity="0.9"/>
            <circle cx="175" cy="100" r="12" fill="#F5F5F5"/><circle cx="175" cy="100" r="8" fill="#B0B0B0"/><circle cx="175" cy="100" r="4" fill="#505050"/>
            <circle cx="225" cy="100" r="12" fill="#F5F5F5"/><circle cx="225" cy="100" r="8" fill="#B0B0B0"/><circle cx="225" cy="100" r="4" fill="#505050"/>
            <path d="M 180 140 Q 200 130 220 140" stroke="#A9A9A9" stroke-width="2" fill="none"/>
            <ellipse cx="200" cy="240" rx="60" ry="80" fill="#D3D3D3" stroke="#A9A9A9" stroke-width="2" opacity="0.8" transform="translate(0, 10) skewY(-15)"/>
            <line x1="140" y1="220" x2="80" y2="240" stroke="#C8C8C8" stroke-width="12" stroke-linecap="round" opacity="0.6"/>
            <line x1="260" y1="220" x2="320" y2="240" stroke="#C8C8C8" stroke-width="12" stroke-linecap="round" opacity="0.6"/>
            <line x1="170" y1="310" x2="165" y2="400" stroke="#6B4423" stroke-width="12" stroke-linecap="round" opacity="0.7"/>
            <line x1="230" y1="310" x2="235" y2="400" stroke="#6B4423" stroke-width="12" stroke-linecap="round" opacity="0.7"/>
            <ellipse cx="165" cy="410" rx="20" ry="10" fill="#654321" opacity="0.7"/><ellipse cx="235" cy="410" rx="20" ry="10" fill="#654321" opacity="0.7"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="15" fill="#FFA500" stroke="#FF8C00" stroke-width="2"/><text x="-2" y="7" font-size="18" fill="white">↓</text></g>
            <text x="200" y="480" text-anchor="middle" font-size="11" fill="#FF8C00" font-weight="bold">Pale • Weak Posture</text>
        </svg>'''
    
    def _iron(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <circle cx="200" cy="120" r="70" fill="#E0D0C8" stroke="#999999" stroke-width="2" opacity="0.85"/>
            <circle cx="175" cy="100" r="12" fill="#F0F0F0" opacity="0.7"/><circle cx="175" cy="100" r="8" fill="#CCCCCC"/><circle cx="175" cy="100" r="4" fill="#555555"/>
            <circle cx="225" cy="100" r="12" fill="#F0F0F0" opacity="0.7"/><circle cx="225" cy="100" r="8" fill="#CCCCCC"/><circle cx="225" cy="100" r="4" fill="#555555"/>
            <ellipse cx="200" cy="145" rx="18" ry="12" fill="#FFCCCC" stroke="#FF9999" stroke-width="1" opacity="0.6"/>
            <path d="M 180 140 Q 200 128 220 140" stroke="#999999" stroke-width="2" fill="none"/>
            <rect x="140" y="200" width="120" height="100" rx="20" fill="#C0C0C0" stroke="#808080" stroke-width="2" opacity="0.75"/>
            <line x1="140" y1="240" x2="60" y2="300" stroke="#E0D0C8" stroke-width="14" stroke-linecap="round" opacity="0.7"/>
            <line x1="260" y1="240" x2="340" y2="300" stroke="#E0D0C8" stroke-width="14" stroke-linecap="round" opacity="0.7"/>
            <line x1="165" y1="300" x2="160" y2="405" stroke="#654321" stroke-width="11" stroke-linecap="round" opacity="0.8"/>
            <line x1="235" y1="300" x2="240" y2="405" stroke="#654321" stroke-width="11" stroke-linecap="round" opacity="0.8"/>
            <ellipse cx="160" cy="410" rx="22" ry="8" fill="#654321" opacity="0.7"/><ellipse cx="240" cy="410" rx="22" ry="8" fill="#654321" opacity="0.7"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="15" fill="#FFB6C1" stroke="#FF69B4" stroke-width="2"/><text x="-3" y="6" font-size="18" fill="white">Z</text></g>
            <text x="200" y="480" text-anchor="middle" font-size="11" fill="#FF69B4" font-weight="bold">Pale Lips • Fatigue</text>
        </svg>'''
    
    def _b12(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <circle cx="200" cy="120" r="70" fill="#E8D4C0" stroke="#A0A0A0" stroke-width="2" opacity="0.9"/>
            <circle cx="175" cy="100" r="12" fill="#FFFACD" opacity="0.8"/><circle cx="175" cy="100" r="8" fill="#FFD700" opacity="0.9"/><circle cx="173" cy="100" r="4" fill="#222222"/>
            <circle cx="225" cy="100" r="12" fill="#FFFACD" opacity="0.8"/><circle cx="225" cy="100" r="8" fill="#FFD700" opacity="0.9"/><circle cx="227" cy="100" r="4" fill="#222222"/>
            <path d="M 180 142 Q 200 132 220 142" stroke="#808080" stroke-width="2" fill="none"/>
            <rect x="140" y="200" width="120" height="100" rx="20" fill="#D3D3D3" stroke="#A9A9A9" stroke-width="2" opacity="0.85" transform="rotate(-5 200 250)"/>
            <polyline points="140,220 120,240 100,230 80,250" stroke="#E8D4C0" stroke-width="14" fill="none" stroke-linecap="round" opacity="0.8"/>
            <polyline points="260,220 280,240 300,230 320,250" stroke="#E8D4C0" stroke-width="14" fill="none" stroke-linecap="round" opacity="0.8"/>
            <path d="M 165 300 Q 160 350 158 400" stroke="#654321" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.8"/>
            <path d="M 235 300 Q 245 350 248 400" stroke="#654321" stroke-width="12" fill="none" stroke-linecap="round" opacity="0.8"/>
            <ellipse cx="158" cy="410" rx="18" ry="8" fill="#654321" opacity="0.75"/><ellipse cx="248" cy="410" rx="18" ry="8" fill="#654321" opacity="0.75"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="15" fill="#FF6347" stroke="#DC143C" stroke-width="2"/><text x="-4" y="7" font-size="18" fill="white">⚡</text></g>
            <text x="200" y="480" text-anchor="middle" font-size="11" fill="#DC143C" font-weight="bold">Tremors • Unsteady</text>
        </svg>'''
    
    def _zinc(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <circle cx="200" cy="120" r="70" fill="#E8C4B0" stroke="#A08070" stroke-width="2"/>
            <path d="M 140 70 Q 150 40 170 50" stroke="#8B4513" stroke-width="2" opacity="0.5"/>
            <path d="M 160 50 Q 175 30 190 45" stroke="#8B4513" stroke-width="2" opacity="0.5"/>
            <path d="M 210 45 Q 225 35 240 50" stroke="#8B4513" stroke-width="2" opacity="0.5"/>
            <path d="M 255 50 Q 270 45 280 65" stroke="#8B4513" stroke-width="2" opacity="0.5"/>
            <circle cx="175" cy="100" r="12" fill="#F5F5F5"/><circle cx="175" cy="100" r="8" fill="#B8860B"/><circle cx="175" cy="100" r="4" fill="#333333"/>
            <circle cx="225" cy="100" r="12" fill="#F5F5F5"/><circle cx="225" cy="100" r="8" fill="#B8860B"/><circle cx="225" cy="100" r="4" fill="#333333"/>
            <circle cx="145" cy="110" r="8" fill="#CD5C5C" opacity="0.7" stroke="#8B3A3A" stroke-width="1"/>
            <circle cx="255" cy="110" r="8" fill="#CD5C5C" opacity="0.7" stroke="#8B3A3A" stroke-width="1"/>
            <path d="M 180 140 Q 200 130 220 140" stroke="#8B4513" stroke-width="2" fill="none"/>
            <rect x="140" y="200" width="120" height="100" rx="20" fill="#D2B48C" stroke="#8B7355" stroke-width="2"/>
            <ellipse cx="160" cy="240" rx="20" ry="25" fill="#FF7F50" opacity="0.5"/><ellipse cx="240" cy="260" rx="18" ry="22" fill="#FF7F50" opacity="0.5"/>
            <line x1="140" y1="230" x2="80" y2="260" stroke="#E8C4B0" stroke-width="15" stroke-linecap="round"/><line x1="260" y1="230" x2="320" y2="260" stroke="#E8C4B0" stroke-width="15" stroke-linecap="round"/>
            <line x1="160" y1="300" x2="160" y2="400" stroke="#654321" stroke-width="12" stroke-linecap="round"/><line x1="240" y1="300" x2="240" y2="400" stroke="#654321" stroke-width="12" stroke-linecap="round"/>
            <ellipse cx="160" cy="410" rx="20" ry="10" fill="#654321"/><ellipse cx="240" cy="410" rx="20" ry="10" fill="#654321"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="15" fill="#FF4500" stroke="#DC143C" stroke-width="2"/><text x="-3" y="6" font-size="18" fill="white">🔥</text></g>
            <text x="200" y="480" text-anchor="middle" font-size="11" fill="#DC143C" font-weight="bold">Dermatitis • Hair Loss</text>
        </svg>'''
    
    def _vitamin_c_toxicity(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <circle cx="200" cy="250" r="200" fill="#FF0000" opacity="0.1"/>
            <circle cx="200" cy="120" r="70" fill="#FF6B6B" stroke="#DC143C" stroke-width="3"/>
            <circle cx="175" cy="100" r="15" fill="#FFFFFF" stroke="#FF0000" stroke-width="2"/><circle cx="175" cy="100" r="8" fill="#000000"/>
            <circle cx="225" cy="100" r="15" fill="#FFFFFF" stroke="#FF0000" stroke-width="2"/><circle cx="225" cy="100" r="8" fill="#000000"/>
            <circle cx="200" cy="145" r="12" fill="#8B0000" stroke="#DC143C" stroke-width="2"/>
            <rect x="140" y="200" width="120" height="100" rx="20" fill="#FF8C8C" stroke="#DC143C" stroke-width="3" opacity="0.9"/>
            <g transform="translate(200, 250)">
                <line x1="-30" y1="0" x2="-60" y2="-10" stroke="#FFB6C1" stroke-width="14" stroke-linecap="round"/>
                <circle cx="-65" cy="-15" r="10" fill="#FFB6C1"/>
                <line x1="30" y1="0" x2="60" y2="-10" stroke="#FFB6C1" stroke-width="14" stroke-linecap="round"/>
                <circle cx="65" cy="-15" r="10" fill="#FFB6C1"/>
                <ellipse cx="0" cy="0" rx="25" ry="35" fill="#8B0000" opacity="0.6" stroke="#FF0000" stroke-width="2"/>
            </g>
            <line x1="140" y1="230" x2="100" y2="190" stroke="#FFB6C1" stroke-width="16" stroke-linecap="round"/>
            <line x1="260" y1="230" x2="300" y2="190" stroke="#FFB6C1" stroke-width="16" stroke-linecap="round"/>
            <line x1="160" y1="300" x2="162" y2="405" stroke="#654321" stroke-width="12" stroke-linecap="round" opacity="0.9"/>
            <line x1="240" y1="300" x2="238" y2="405" stroke="#654321" stroke-width="12" stroke-linecap="round" opacity="0.9"/>
            <ellipse cx="162" cy="410" rx="20" ry="10" fill="#654321"/><ellipse cx="238" cy="410" rx="20" ry="10" fill="#654321"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="18" fill="#FF0000" stroke="#8B0000" stroke-width="3"/><text x="-6" y="8" font-size="22" fill="white" font-weight="bold">!</text></g>
            <text x="200" y="480" text-anchor="middle" font-size="11" fill="#FF0000" font-weight="bold">TOXICITY ALERT</text>
        </svg>'''
    
    def _iodine(self):
        return '''<svg width="400" height="500" xmlns="http://www.w3.org/2000/svg">
            <circle cx="200" cy="120" r="70" fill="#E8D4C0" stroke="#999999" stroke-width="2" opacity="0.9"/>
            <circle cx="175" cy="100" r="12" fill="#F0F0F0" opacity="0.7"/><circle cx="175" cy="100" r="8" fill="#CCCCCC"/><circle cx="175" cy="100" r="4" fill="#555555"/>
            <circle cx="225" cy="100" r="12" fill="#F0F0F0" opacity="0.7"/><circle cx="225" cy="100" r="8" fill="#CCCCCC"/><circle cx="225" cy="100" r="4" fill="#555555"/>
            <path d="M 180 140 Q 200 125 220 140" stroke="#999999" stroke-width="2" fill="none"/>
            <ellipse cx="200" cy="180" rx="50" ry="35" fill="#D8BFD8" stroke="#8B7BA8" stroke-width="2" opacity="0.8"/>
            <ellipse cx="200" cy="175" rx="45" ry="30" fill="#DDA0DD" opacity="0.6"/>
            <path d="M 175 175 Q 200 185 225 175" stroke="#8B7BA8" stroke-width="1" opacity="0.6"/>
            <rect x="130" y="210" width="140" height="110" rx="20" fill="#C8C8C8" stroke="#808080" stroke-width="2" opacity="0.85"/>
            <line x1="130" y1="240" x2="50" y2="280" stroke="#E8D4C0" stroke-width="18" stroke-linecap="round" opacity="0.85"/>
            <line x1="270" y1="240" x2="350" y2="280" stroke="#E8D4C0" stroke-width="18" stroke-linecap="round" opacity="0.85"/>
            <line x1="155" y1="320" x2="155" y2="405" stroke="#654321" stroke-width="14" stroke-linecap="round" opacity="0.85"/>
            <line x1="245" y1="320" x2="245" y2="405" stroke="#654321" stroke-width="14" stroke-linecap="round" opacity="0.85"/>
            <ellipse cx="155" cy="410" rx="24" ry="10" fill="#654321" opacity="0.85"/><ellipse cx="245" cy="410" rx="24" ry="10" fill="#654321" opacity="0.85"/>
            <g transform="translate(280, 150)"><circle cx="0" cy="0" r="15" fill="#9370DB" stroke="#8B7BA8" stroke-width="2"/><text x="-3" y="6" font-size="18" fill="white">😴</text></g>
            <text x="200" y="480" text-anchor="middle" font-size="11" fill="#8B7BA8" font-weight="bold">Goiter • Lethargy</text>
        </svg>'''
    
    def get_svg(self, state):
        return self.avatars.get(state, self.avatars["healthy"])
    
    def render_in_streamlit(self, state):
        svg_code = self.get_svg(state)
        st.image(f"data:image/svg+xml;charset=utf-8;base64,{base64.b64encode(svg_code.encode()).decode()}", use_column_width=True)
