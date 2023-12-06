# Overview

## Relevant Paper

**JUIndoorLoc**: A Ubiquitous Framework for Smartphone-Based Indoor Localization Subject to Context and Device Heterogeneity

## Dataset Description

- The data has been captured from the third and fifth floors of a five-storied building at Jadavpur University
- JUIndoorLoc dataset, containing 25,364 samples, is divided into two datasets:
    - Training(23,904 samples)
    - Testing(1,460 samples)
- Each sample of the two datasets consists of 177 attributes. These attributes containRSSI values of 172 wireless access points (AP) along with the corresponding location point (cell) identifier, time, device identifier and contextual changes (open/closed room and presence/absence of the user in the
  vicinity).
- The RSSI values are represented as negative integer values ranging -11dBm to -100dBm (extremely weak signal). A negative value -110 is used to denote when anAP was not detected.

## Attributes Information of JUIndoorLoc dataset

<table>
  <tr>
    <th>Attribute</th>
    <th>MySQL data type</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>C<sub>ID</sub></td>
    <td>VARCHAR(15)</td>
    <td>A unique number to identify the indoor region where the capture is taken. Each cell number has two parts, the first part is floor number, and the second part is the position of a cell on the two-dimensional building map.</td>
  </tr>
  <tr>
    <td>AP<sub>Number</sub></td>
    <td>INT(4)</td>
    <td>Received signal strength value of 172 APs. Negative integer values from -11dBm to -100dBm and -110 used to identify the APs which are not detected in scan duration.</td>
  </tr>
  <tr>
    <td>R<sub>S</sub></td>
    <td>BOOL</td>
    <td>Represents the status of the room, the value is either one or zero. One and zero represent open and closed room respectively.</td>
  </tr>
  <tr>
    <td>H<sub>pr</sub></td>
    <td>BOOL</td>
    <td>Represents the presence or absence of human, the value is either one or zero. One and zero represent the presence and absence of humans respectively.</td>
  </tr>
  <tr>
    <td>D<sub>ID</sub></td>
    <td>VARCHAR(10)</td>
    <td>A unique identifier is assigned to each Android device, which is used to capture data. These device Identifiers are given below :
    <ul>
      <li><b>D<sub>1</sub></b>: Samsung Galaxy Tab 2, Android version 4.1.1</li>
      <li><b>D<sub>2</sub></b>: Samsung Galaxy Tab E, Android version 5.0</li>
      <li><b>D<sub>3</sub></b>: Samsung Galaxy Tab 10, Android version 4.0</li>
      <li><b>D<sub>4</sub></b>: Motorola Moto E 2nd Generation, Android version 5.1 </li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>T<sub>S</sub></td>
    <td>BIGINT(8)</td>
    <td>13-digit integer value used to record time when the capture is taken following library of java.util package.</td>
  </tr>
</table>
