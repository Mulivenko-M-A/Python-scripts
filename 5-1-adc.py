def binarize(number):
  bin_number=[int(i) for i in bin(number)[2:].zfill(8)]
  return bin_number

def adc_sar():
  value=127
  for i in range(-6,1):
    i=-i
    GPIO.output(dac,binarize(value))
    t.sleep(0.02)
    if GPIO.input(comp):value+=-(2**i)
    else:value+=(2**i)
    return value
