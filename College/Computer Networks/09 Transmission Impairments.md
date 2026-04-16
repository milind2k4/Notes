Links: [[00 Computer Networks]], [[08 Physical Layer]], [[03 Transmission Media]]
___
# Transmission Impairments

A signal traveling through transmission media is not perfect; it deteriorates over distance. This deterioration of the quality of an analog signal is called a **transmission impairment**. It means the signal received at the destination is not the exact same signal that was transmitted by the source.

There are three main causes of network impairments:

## Attenuation
Attenuation means a **loss of energy**. When a signal travels through a medium, it loses some of its energy in overcoming the resistance of the medium (converting it into heat). 

> [!NOTE] Signal Strength
> Signal strength is inversely proportional to distance. As distance increases, attenuation increases.

To compensate for this loss, amplifiers are used to boost the signal.

### Measuring Attenuation
Attenuation is measured in **Decibels (dB)**, which measures the relative strengths of two signals or a single signal at two different points.

$$ \text{Attenuation (dB)} = 10 \log_{10} \frac{P_2}{P_1} $$

Where:
-   $P_1$ = Power of the signal at point 1 (source).
-   $P_2$ = Power of the signal at point 2 (destination).

*(Note: Since $P_2 < P_1$ due to loss, the dB result is usually negative, indicating attenuation).*

## Distortion
Distortion means **changes in the form or shape** of the signal. It often occurs in composite signals (signals made of multiple frequencies).

-   Each frequency component has its own propagation speed traveling through a medium and, therefore, its own delay in arriving at the final destination.
-   Because different frequencies arrive at different times, the overall shape of the composite signal is altered (distorted).

## 3. Noise
**Noise** is any random or unwanted signal that mixes with the original signal, altering its wave shape.

### Types of Noise
1.  **Thermal Noise:** Caused by the random motion of electrons in wires. This motion creates an extra, unwanted signal even if no voltage is applied.
2.  **Induced Noise:** Comes from external sources such as motors or appliances acting as transmitting antennas, and the transmission medium acting as the receiving antenna.
3.  **Crosstalk:** The effect of one wire on another. For example, hearing another conversation on the telephone line. (This is why wires in twisted-pair cables are physically twisted).
4.  **Impulse Noise:** A spike (a signal with high energy in a very short time) that comes from lightning or power lines.
