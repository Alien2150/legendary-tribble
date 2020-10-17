#include <ezButton.h>
#include <simpleRPC.h>
#include "types.tcc"

// Define consts 
#define MAX_BUTTONS 3
#define STARTING_PIN 2

HardwareSerialIO io;
ezButton buttons[MAX_BUTTONS] = {
	ezButton(STARTING_PIN+0),
	ezButton(STARTING_PIN+1),
	ezButton(STARTING_PIN+2)
	
};

void setup() {
	pinMode(LED_BUILTIN, OUTPUT);
	Serial.begin(9600);
	io.begin(Serial);


	for (int idx = 0; idx < MAX_BUTTONS; idx++) {
		buttons[idx].setDebounceTime(50);
		buttons[idx].setCountMode(COUNT_RISING);
    }
}

Vector<int> getButtonCount() {
	Vector<int> r(MAX_BUTTONS);

    for (int idx = 0; idx < MAX_BUTTONS; idx++) {
		// counts
		r[idx] = buttons[idx].getCount(); 	
    }

    return r;
}

void resetButtonCount() {
   	// reset buttons 
   	for (int idx = 0; idx < MAX_BUTTONS; idx++) {
		buttons[idx].resetCount(); 	
	}
}


void loop() { 
    interface(io, 
        getButtonCount, F("button_state: Get button state. @return: The button-state"),
        resetButtonCount, F("reset_button_state: Reset button state")
    );

  	
    for (int idx = 0; idx < MAX_BUTTONS; idx++) {
		buttons[idx].loop();
		if (buttons[idx].isPressed()) {
			digitalWrite(LED_BUILTIN, HIGH);
			delay(500);
			digitalWrite(LED_BUILTIN, LOW);
		}
    }
}
