let input = window.document.getElementsByName('orderNo')[0];
let lastValue = input.value;
input.value = arguments[0];
let event = new Event('input', { bubbles: true });
event.simulated = true;
let tracker = input._valueTracker;
if (tracker) {
      tracker.setValue(lastValue);
}
input.dispatchEvent(event);
let input2 = window.document.getElementsByName('email')[0];
let lastValue2 = input2.value;
input2.value = arguments[1];
let event2 = new Event('input2', { bubbles: true });
event2.simulated = true;
let tracker2 = input2._valueTracker;
if (tracker2) {
      tracker2.setValue(lastValue2);
}
input2.dispatchEvent(event);
window.document.getElementsByClassName('gl-cta gl-cta--primary order-tracker__submit___2oWVr')[0].click()