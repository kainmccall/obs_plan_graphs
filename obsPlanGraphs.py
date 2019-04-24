# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 10:48:56 2019

@author: Kain
Include ability to plot the timing of multiple points on the light curve by making an array of initialPoints, each corresponding to a title and then given by a legend...? Could be good...
"""
import numpy as np
import wx
#from PyAstronomy import pyasl #do I need to worry about converting to HJD??? I don't think so, as long as the user has inuput their date in HJD...
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz, get_sun

def obsPlanGraphs(targetCoords, observatoryCoords, utc_offset, period, initialPoint, startDay, **kwargs):
    if "nRows" in kwargs:
        rows = kwargs["nRows"]
    else:
        rows = 8
    columns = 3
    saveText = False
    saveImg = False
    if "saveFile" in kwargs:
        saveText = True
        filename = kwargs["saveFile"]
    if "saveFig" in kwargs:
        saveImg = True
        figname = kwargs["saveFig"]
    startDay1 = startDay + ' 00:00:00'
    utcoffset = utc_offset*u.hour
    latitude, longitude, elev = observatoryCoords
    rightascent, declin = targetCoords
    observatory = EarthLocation(lat=latitude*u.deg, lon=longitude*u.deg, height=elev*u.m)
    midnight = Time(startDay1) - utcoffset
    midnight1 = midnight.to_datetime()
    target = SkyCoord(ra=rightascent*u.degree, dec=declin*u.degree)
    numDays = rows * columns
    initialDatetime = Time(initialPoint, format='jd').to_datetime()
    dayDiff1 = midnight1 - initialDatetime
    dayDiff = dayDiff1.days
    numPoints = int((1/period)*(numDays + dayDiff + 2))
    isVisible = np.zeros(numPoints, dtype=bool)
    isGraphed = np.zeros(numPoints, dtype=bool)
    brightestJD = np.zeros(numPoints)
    brightTime = np.zeros(numPoints)
    if saveText:
        header = "{:15} {:15} {:20} {:10}".format("Date", "Local Time", "Altitude", "Observable")
        retFile = open(filename, "w")
        retFile.write(header)
        retFile.close()
    for i in range(numPoints):
        brightestJD[i] = initialPoint + (period * i)
        t = Time(brightestJD[i], format='jd')
        t1 = t.to_datetime()
        t2 = t1 - midnight1
        brightTime[i] = ((t2.days * 24 * 3600) + t2.seconds) / 3600
    currentDay = midnight
    newFig = plt.figure(figsize=(12,3*rows))
    for i in range(1, (rows * columns) + 1):
        newFig.add_subplot(rows, columns, i)
        plt.tight_layout()
        delta_midnight = np.linspace(-12, 12, 1000)*u.hour
        times = currentDay + delta_midnight
        altazframe = AltAz(obstime=times, location=observatory)
        sunaltazs = get_sun(times).transform_to(altazframe)
        targetaltazs = target.transform_to(altazframe)
        dateString = str(currentDay)
        if "targetName" in kwargs:
            graphTitle = str(kwargs["targetName"]) + " on " + dateString[0:10]
        else:
            graphTitle = "Target on " + dateString[0:10]
        plt.plot(delta_midnight, targetaltazs.alt, color='y')
        plt.xlim(-12, 12)
        plt.ylim(0, 90)
        if "altLim" in kwargs:
            plt.axhline(y=kwargs["altLim"], color='b')
            aLim = kwargs["altLim"]*u.deg
        else:
            aLim = 0*u.deg
        plt.fill_between(delta_midnight.to('hr').value, 0, 90, sunaltazs.alt<-0*u.deg, color='0.5', zorder=0)
        plt.fill_between(delta_midnight.to('hr').value, 0, 90, sunaltazs.alt < -18*u.deg, color='k', zorder=0)
        printAll = False
        if "printMax" in kwargs:
            printAll = kwargs["printMax"]
        printDate = currentDay + brightTime*u.hour + utcoffset
        localFrame = AltAz(obstime=printDate - utcoffset, location=observatory)
        tAltAz = target.transform_to(localFrame)
        sAltAz = get_sun(printDate-utcoffset).transform_to(localFrame)
        for j in range(numPoints):
            if sAltAz.alt[j]<-0*u.deg and tAltAz.alt[j]>=aLim:
                isVisible[j]=True
            else:
                isVisible[j]=False
            if brightTime[j] <= 12 and brightTime[j] >= -12:
                isGraphed[j] = True
                plt.axvline(x=brightTime[j], color='r')
                if printAll:
                    print("Date & Time (Local): " + str(printDate[j]))
                    print("Target Altitude: " + str(tAltAz.alt[j]))
                    print("Is Observable: " + str(isVisible[j]))
                    print("\n")
            else:
                isGraphed[j] = False
            brightTime[j] = brightTime[j] - 24
        if saveText:
            retFile = open(filename, "a")
            for k in range(numPoints):
                if isGraphed[k]:
                    retFile.write("\n")
                    dataLine = "%-15s %-15s %-20s %-10s" % (str(printDate[k])[0:10], str(printDate[k])[11:22], tAltAz.alt[k], isVisible[k])
                    retFile.write(dataLine)
            retFile.close()
        plt.xlabel("Hours Since Midnight (Local Time)")
        plt.ylabel("Altitude (degrees)")
        plt.title(graphTitle)
        currentDay = currentDay + 1*u.d
    if saveImg:
        plt.savefig(figname)
    plt.savefig("temp.png")
    #wx.Image("temp.png", wx.BITMAP_TYPE_ANY).ComvertToBitmap()
    plt.show()

def obsPlanGraph(targetCoords, observatoryCoords, utc_offset, period, initialPoint, startDay, **kwargs):
    saveImg = False
    if "saveFig" in kwargs:
        saveImg = True
        figname = kwargs["saveFig"]    
    startDay1 = startDay + ' 00:00:00'
    utcoffset = utc_offset*u.hour
    latitude, longitude, elev = observatoryCoords
    rightascent, declin = targetCoords
    observatory = EarthLocation(lat=latitude*u.deg, lon=longitude*u.deg, height=elev*u.m)
    midnight = Time(startDay1) - utcoffset
    midnight1 = midnight.to_datetime()
    target = SkyCoord(ra=rightascent*u.degree, dec=declin*u.degree)
    numDays = 1
    initialDatetime = Time(initialPoint, format='jd').to_datetime()
    dayDiff1 = midnight1 - initialDatetime
    dayDiff = dayDiff1.days
    numPoints = int((1/period)*(numDays + dayDiff + 2))
    isVisible = np.zeros(numPoints, dtype=bool)    
    brightestJD = np.zeros(numPoints)
    brightTime = np.zeros(numPoints)
    for i in range(numPoints):
        brightestJD[i] = initialPoint + (period * i)
        t = Time(brightestJD[i], format='jd')
        t1 = t.to_datetime()
        t2 = t1 - midnight1
        brightTime[i] = ((t2.days * 24 * 3600) + t2.seconds) / 3600
    currentDay = midnight
    delta_midnight = np.linspace(-12, 12, 1000)*u.hour
    times = currentDay + delta_midnight
    altazframe = AltAz(obstime=times, location=observatory)
    sunaltazs = get_sun(times).transform_to(altazframe)
    targetaltazs = target.transform_to(altazframe)
    dateString = str(currentDay)
    if "targetName" in kwargs:
        graphTitle = str(kwargs["targetName"]) + " on " + dateString[0:10]
    else:
        graphTitle = "Target on " + dateString[0:10]
    plt.plot(delta_midnight, targetaltazs.alt, color='y')
    plt.xlim(-12, 12)
    plt.ylim(0, 90)
    if "altLim" in kwargs:
        plt.axhline(y=kwargs["altLim"], color='b')
        aLim = kwargs["altLim"]*u.deg
    else:
        aLim = 0*u.deg
    plt.fill_between(delta_midnight.to('hr').value, 0, 90, sunaltazs.alt<-0*u.deg, color='0.5', zorder=0)
    plt.fill_between(delta_midnight.to('hr').value, 0, 90, sunaltazs.alt < -18*u.deg, color='k', zorder=0)
    printAll = False
    if "printMax" in kwargs:
        printAll = kwargs["printMax"]
    printDate = currentDay + brightTime*u.hour + utcoffset
    localFrame = AltAz(obstime=printDate - utcoffset, location=observatory)
    tAltAz = target.transform_to(localFrame)
    sAltAz = get_sun(printDate-utcoffset).transform_to(localFrame)
    for j in range(numPoints):
        if sAltAz.alt[j]<-0*u.deg and tAltAz.alt[j]>=aLim:
            isVisible[j]=True
        else:
            isVisible[j]=False
        if brightTime[j] <= 12 and brightTime[j] >= -12:
            plt.axvline(x=brightTime[j], color='r')
            if printAll:
                print("Date & Time (Local): " + str(printDate[j]))
                print("Target Altitude: " + str(tAltAz.alt[j]))
                print("Is Observable: " + str(isVisible[j]))
                print("\n")
    plt.xlabel("Hours Since Midnight (Local Time)")
    plt.ylabel("Altitude (degrees)")
    plt.title(graphTitle)
    if saveImg:
        plt.savefig(figname)
    plt.savefig("temp.png")
    #wx.Image("temp.png", wx.BITMAP_TYPE_ANY).ComvertToBitmap()
    plt.show()