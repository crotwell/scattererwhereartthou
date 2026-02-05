
import pytest

from scattererwhereartthou import spherical

def test_polar():
    pole_lat=90
    pole_lon=0
    eq_lat=0
    eq_lon=0
    d, az, baz = spherical.distaz_deg(eq_lat, eq_lon, pole_lat, pole_lon)
    assert d == 90.0
    assert az == 0
    assert baz == 180

def test_halfdist():
    """ copy from SphericalCoordsTest in TauP java """

    stationLat = 37.18
    stationLon = 21.92
    eventLat = -17.84
    eventLon = -178.30
    dist, azimuth, backAzimuth = spherical.distaz_deg(eventLat,
                                             eventLon,
                                             stationLat,
                                             stationLon)

    assert (dist) == pytest.approx(153.74, abs=1e-2)
    assert (azimuth) == pytest.approx(-38.50, abs=1e-2)
    assert (backAzimuth) == pytest.approx(48.05, abs=1e-2)

    lat, lon = spherical.latLonFor(eventLat,
                                 eventLon,
                                 dist,
                                 azimuth);
    assert (lat) == pytest.approx(stationLat, abs=1e-2)
    assert (lon) == pytest.approx(stationLon, abs=1e-2)

    halfdist = 38.34
    lat, lon = spherical.latLonFor(eventLat,
                                 eventLon,
                                 halfdist,
                                 azimuth);
    assert (lat) == pytest.approx(12.82, abs=1e-2)
    assert (lon) == pytest.approx(158.37, abs=1e-2)
    d, az, baz = spherical.distaz_deg(eventLat,
                                           eventLon, 12.82, 158.37)
    assert (az) == pytest.approx(azimuth, abs=1e-2)
    assert (d) == pytest.approx(halfdist, abs=1e-2)
