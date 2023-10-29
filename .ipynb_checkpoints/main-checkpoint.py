import  stringify
if __name__ == '__main__':
    test = stringify.stringify("Year, Quarter, Month, DayofMonth, DayOfWeek, FlightDate, Reporting_Airline, Origin, OriginState, Dest, DestState, CRSDepTime, DepDelayMinutes, DepartureDelayGroups, Cancelled, Diverted, Distance, DistanceGroup, ArrDelay, ArrDelayMinutes, ArrDel15, AirTime", ",")
    print(test)
