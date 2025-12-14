import streamlit.components.v1 as components

def show():
    components.html("""
    <style>
    
    #animation-container {

        height: 100vh;
        overflow: visible;
        transform: scale(var(--scale));
    }

    #animation-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    --scale: 0.5;

    
    .star {
    width: 50px;
    aspect-ratio: 1;
    background: #d68910;
    clip-path: polygon(50% 0, 79% 90%, 2% 35%, 98% 35%, 21% 90%);
    }

    .level {
    display: flex;
    justify-content: center;
    align-items: center;
    }

    .circle {
    width: 30px;
    height: 30px;
    background-color: aliceblue;
    border-radius: 50%;
    margin: 5px;
    transition: background-color 0.3s ease;
    }

    .toggle-switch {
    position: relative;
    height: 30px;
    border-radius: 30px;
    transition: background-color 0.3s ease;
    margin: 0 5px;
    cursor: pointer;
    }

    .toggle-circle {
    position: absolute;
    width: 30px;
    height: 30px;
    background: #ff6b35;
    border-radius: 50%;
    transition: transform 0.3s ease, background-color 0.3s ease;
    }

    .toggle-switch-s {
    width: 70px;
    }

    .toggle-switch-m {
    width: 95px;
    }

    .toggle-switch-l {
    width: 110px;
    }

    }


    </style>
    <div id="animation-container">
    <div class="star"></div>
    <div class="level" id="level-1">
        <div class="circle"></div>
    </div>
    <div class="level" id="level-2">
        <div class="circle"></div>
        <div class="circle"></div>
    </div>
    <div class="level" id="level-3">
        <div class="toggle-switch toggle-switch-s" data-size="70">
        <div class="toggle-circle"></div>
        </div>
        <div class="circle"></div>
    </div>
    <div class="level" id="level-4">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="toggle-switch toggle-switch-s" data-size="70">
        <div class="toggle-circle"></div>
        </div>
    </div>
    <div class="level" id="level-5">
        <div class="circle"></div>
        <div class="toggle-switch toggle-switch-l" data-size="110">
        <div class="toggle-circle"></div>
        </div>
        <div class="circle"></div>
    </div>
    <div class="level" id="level-6">
        <div class="toggle-switch toggle-switch-s" data-size="70">
        <div class="toggle-circle"></div>
        </div>
        <div class="circle"></div>
        <div class="toggle-switch toggle-switch-s" data-size="70">
        <div class="toggle-circle"></div>
        </div>
        <div class="circle"></div>
    </div>
    <div class="level" id="level-7">
        <div class="circle"></div>
        <div class="toggle-switch toggle-switch-m" data-size="95">
        <div class="toggle-circle"></div>
        </div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
    </div>
    <div class="level" id="level-8">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="toggle-switch toggle-switch-l" data-size="110">
        <div class="toggle-circle"></div>
        </div>
        <div class="circle"></div>
    </div>
    <div class="level" id="level-9">
        <div class="toggle-switch toggle-switch-s" data-size="70">
        <div class="toggle-circle"></div>
        </div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="toggle-switch toggle-switch-m" data-size="95">
        <div class="toggle-circle"></div>
        </div>
    </div>
    </div>
    <script>// Inspiration https://pin.it/54OtjL2BT

    const COLORS = ["#c0392b", "#f8f9fa", "#d68910", "#0e6655", "#27ae60"];
    const TOGGLE_CIRCLE_SIZE = 30;
    const ANIMATION_INTERVAL = 1000;

    const toggles = document.querySelectorAll(".toggle-switch");
    const circles = document.querySelectorAll(".circle");

    let counter = 0;

    // Store color pairs for each element
    const circleColors = new Map();
    const toggleBackgroundColors = new Map();
    const toggleCircleColors = new Map();

    const getTwoRandomColors = () => {
    const first = Math.floor(Math.random() * COLORS.length);
    let second = Math.floor(Math.random() * COLORS.length);

    while (second === first) {
        second = Math.floor(Math.random() * COLORS.length);
    }

    return [COLORS[first], COLORS[second]];
    };

    const getUniqueColorPairs = () => {
    const pair1 = getTwoRandomColors();
    let pair2 = getTwoRandomColors();

    // Ensure pair2 doesn't share any colors with pair1
    while (pair2.includes(pair1[0]) || pair2.includes(pair1[1])) {
        pair2 = getTwoRandomColors();
    }

    return [pair1, pair2];
    };

    // Initialize colors for each circle element
    circles.forEach((circle) => {
    circleColors.set(circle, getTwoRandomColors());
    });

    toggles.forEach((toggle) => {
    const [bgColors, circleColors] = getUniqueColorPairs();
    toggleBackgroundColors.set(toggle, bgColors);
    toggleCircleColors.set(toggle.querySelector(".toggle-circle"), circleColors);
    });

    const animateToggles = () => {
    toggles.forEach((toggle) => {
        const toggleCircle = toggle.querySelector(".toggle-circle");
        const size = parseInt(toggle.dataset.size);
        const isLarge = toggle.classList.contains("toggle-switch-l");
        // Changing direction of L toggles to make it visually more interesting
        const shouldToggle = isLarge ? counter % 2 === 0 : counter % 2 !== 0;

        const translateX = shouldToggle ? size - TOGGLE_CIRCLE_SIZE : 0;
        const bgColors = toggleBackgroundColors.get(toggle);
        const circleColors = toggleCircleColors.get(toggleCircle);
        const bgColorIdx = shouldToggle ? 1 : 0;
        const circleColorIdx = counter % 2;

        toggle.style.backgroundColor = bgColors[bgColorIdx];
        toggleCircle.style.transform = `translateX(${translateX}px)`;
        toggleCircle.style.backgroundColor = circleColors[circleColorIdx];
    });
    };

    const animateCircles = () => {
    circles.forEach((circle) => {
        const colors = circleColors.get(circle);
        const colorIdx = counter % 2;
        circle.style.backgroundColor = colors[colorIdx];
    });
    };

    const animate = () => {
    counter++;
    animateToggles();
    animateCircles();
    };

    // Initial animation
    animate();

    // Start interval
    setInterval(animate, ANIMATION_INTERVAL);
    </script>
    """, height=300
    )