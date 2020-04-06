let button = document.getElementById('click_button');
let button_timer = document.getElementById('timer')

// FUnction starting timer by running reqursion
function start_timer() {
    milliseconds();
}

// Function that resets score and shows result
function stop_timer() {
    p_result = document.getElementById('score');
    result = parseInt(p_result.innerHTML);
    p_result.innerHTML = '0';
    alert(result);
}

// Function handling milliseconds
function milliseconds() {
    // Get seconds and milliseconds
    ms_span = document.getElementById('milliseconds');
    s_span = document.getElementById('seconds');

    // If time is 0:00 => calling stop timer function with 100 ms timeout
    if ((parseInt(ms_span.innerHTML) == 0) && (parseInt(s_span.innerHTML) == 0)) { 
        setTimeout(
            () => {stop_timer();},100
        );
     }
    // If time is not out 
    else {
        // If ms value is 00 calling decreasing sec function
        // and set ms value to 90 with 100ms delay. Then its calling itself
        if (parseInt(ms_span.innerHTML) == 0) {
            setTimeout(() => {
                seconds();
                ms_span.innerHTML = 90;
                milliseconds();
            }, 100);

        }
        // If ms value != 00, func making 100ms delay,
        // decrease itself value by 10, and calling itself
        else {
            setTimeout(
                () => {
                    ms_span.innerHTML = parseInt(ms_span.innerHTML) - 10;
                    milliseconds();
                }, 100
            );
        }
    }
}

// Function decreasing seconds, when ms = 00
function seconds() {
    s_span = document.getElementById('seconds');
    s_span.innerHTML = parseInt(s_span.innerHTML) - 1;

}

// Function handling click on button
function button_click_handler() {
    let p = document.getElementById('score');
    p_value = parseInt(p.innerHTML);
    p_value += 1;
    p.innerHTML = p_value;
}

button.onclick = button_click_handler;
button_timer.onclick = start_timer;

