
// Book of Shaders - Ch. 7: Shapes

// ------------------------------------------------ VERTEX SHADER --
var vsFlatScreen = `

    void main() {
        gl_Position = vec4( position, 1.0 );
    }
`;

// ------------------------------------------------ FRAGMENT SHADER --
var fsFlatScreen = `

	uniform vec2 u_mouse;
	uniform vec2 u_resolution;
	uniform float u_time;

	void main() {
	    vec2 st = gl_FragCoord.xy / u_resolution.xy;
	    vec2 m = u_mouse.xy / u_resolution.xy;

	    
	    
	    gl_FragColor=vec4(m.x, m.y, 0.2, 1.0);
	}
`;