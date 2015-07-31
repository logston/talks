:title: The Graph To My Hearduino
:author: Paul Logston
:description: A look at wrapping the olimex EKG shield with Python
:keywords: ekg, arduino, olimex, emg, python
:skip-help: true

----

The Graph To My Heardunio
=========================

Paul Logston
------------

|twitter_logo| ...... `@paullogston <https://twitter.com/PaulLogston>`_

.. |twitter_logo| image:: images/twitter-4096-black.png
   :width: 20
   :alt: Twitter Handle

**W^3** ... `plog.logston.me <https://plog.logston.me>`_

----

TOC
===



----

EKG Theory
==========

Crash Course
------------

|ekg_fast|

[1] Primal Pictures

.. |ekg_fast| image:: images/ekg-video.gif
   :height: 500

----

EKG Theory
==========

Crash Course
------------

|ekg_nsr| [2] Medical Training and Simulation LLC

|ekg_graph| [3] ????

.. |ekg_nsr| image:: images/ekg_nsr.gif
   :height: 200

.. |ekg_graph| image:: images/graphpaper.png
   :height: 400

----

Building It
===========

|arduino|

[Arduino]

|olimex_shield|

[Olimex EKG Shield]

.. |arduino| image:: images/arduino.jpg
   :height: 200

.. |olimex_shield| image:: images/olimex_shield.jpg
   :height: 200


- $7 dollar Arduino
- $50 shield
- $20 leads
- $5 red dots
- **$82** TOTAL

----

Writing It
==========

Olimex Shield Output
--------------------

It streams packets that it builds at ``SAMPLE_FREQUENCY`` (125 hz)

::

  //Read the 6 ADC inputs and store current values in Packet
  for(CurrentCh=0;CurrentCh<6;CurrentCh++){
    ADC_Value = analogRead(CurrentCh);
    TXBuf[((2*CurrentCh) + HEADERLEN)] = ((unsigned char)((ADC_Value & 0xFF00) >> 8));  // Write High Byte
    TXBuf[((2*CurrentCh) + HEADERLEN + 1)] = ((unsigned char)(ADC_Value & 0x00FF));     // Write Low Byte
  }

  // Send Packet
  for(TXIndex=0;TXIndex<17;TXIndex++){
  //    Serial.write(TXBuf[TXIndex]);
      Serial.print(TXBuf[TXIndex], HEX);
      Serial.println("");
  }

----

Writing It
==========

Olimex Shield Output
--------------------

::

    struct Olimexino328_packet
    {
      uint8_t       sync0;          // = 0xa5
      uint8_t       sync1;          // = 0x5a
      uint8_t       version;        // = 2 (packet version)
      uint8_t       count;          // packet counter. Increases by 1 each packet.
      uint16_t      data[6];        // 10-bit sample (= 0 - 1023) in big endian (Motorola) format.
      uint8_t       switches;       // State of PD5 to PD2, in bits 3 to 0.
    };

----

Writing It
==========

PySerial
--------

|logo|

==

|bowl|

.. |logo| image:: images/pyserial.png
  :width: 200

.. |bowl| image:: images/giphy_1.gif
  :width: 200


----

Writing It
==========

Reading From Serial Port
------------------------

::

    class PacketStreamReader:
       def __init__(self, serial):
            self._serial = serial

        def _get_next_packet(self):
            byte0, byte1 = 0, 0

            while byte0 != SYNC0 or byte1 != SYNC1:
                # If we don't have enough data to do ALL of the following,
                # return None.
                #   - Move current byte 1 into byte0 position
                #   - Read a new byte into byte1  (1 byte)
                #   - Read the rest of a packet into a buffer (PACKET_SIZE - 2 bytes)
                # We need at least (PACKET_SIZE - 2) + 1 bytes before
                # attempting to get the next packet.
                in_waiting = self._serial.inWaiting()
                if in_waiting < PACKET_SIZE - 1:
                    return None
                byte0, byte1 = byte1, self._serial.read()

            buff = bytearray()
            buff.append(ord(byte0))
            buff.append(ord(byte1))
            # read 15 more bytes
            buff.extend(self._serial.read(PACKET_SIZE -2))
            return buff

----

Writing It
==========

How to we build broken values?
------------------------------

::

    def calculate_values_from_packet_data(data):
       values = []

        for index in range(0, len(data), 2):
            # byte_a is the most significant byte and byte_b is
            # the least significant byte.
            byte_a, byte_b = data[index], data[index + 1]
            val = (byte_a << 8) | byte_b
            # For some reason the data comes in upside down.
            # Flip data around a horizontal axis.
            val = (val - 1024) * -1
            values.append(val)

        return values

----


Using It
========

at the command line...
----------------------

::

    $ exg -p /dev/tty.usbmodem1411

    $ exg -f mock-data/nsr.bin

EXTCHANGE FOR GIF

|olimex_nsr_video|

.. |olimex_nsr_video| image:: images/olimex_nsr.png
  :width: 800

----

Using It
========

Compare
-------

|olimex_nsr|

|lifepak_nsr|

.. |olimex_nsr| image:: images/olimex_nsr.png
  :width: 800

.. |lifepak_nsr| image:: images/lifepak_nsr.jpg
  :width: 800

----

Using It
========

Compare
-------

|olimex_shield| |lifepak|

.. |lifepak| image:: images/lifepak.jpg
  :width: 300

----

Using It
========

Live Demo
---------

Can I get a volunteer?!

|olimex_nsr_video|

----

Analysis
========

Key Points from Live Demo

- Not medical grade
- Nothing but course assessment of pt
- Time drift

----

Thank You
=========

- CPR123

- BOF room


Questions?

----

Bibliography
============

[1]
Anatomy & Physiology Online - Cardiac conduction system and its relationship with ECG
Primal Pictures - 3D Human Anatomy
https://www.youtube.com/watch?v=v3b-YhZmQu8

[2]
Medical Training and Simulation LLC

[3] CPR123
