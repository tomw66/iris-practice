import iris
import matplotlib.pyplot as plt
import iris.plot as iplt
import iris.quickplot as qplt

def temp_plot():
    """
    Extracts air tempearture data, constrains it to a specified time range (averaged) and model level, converts to celsius and plots map. 
    Not sure the averaging actually works...
    """
    filename = '/data/users/ersmith/Temporary_Files/Framework/Example_Data_Files/Model/20200915_Model_Gridded_Data.nc'
    air_temp = iris.load_cube(filename, 'air_temperature')

    day_start = iris.time.PartialDateTime(year=2020, month=9, day=15, hour=12, minute=0)
    day_end = iris.time.PartialDateTime(year=2020, month=9, day=15, hour=13, minute=0)

    day_2d = air_temp.extract(iris.Constraint(time = lambda cell: day_start <= cell.point < day_end, model_level_number = 5))
    day_mean = day_2d.collapsed('time', iris.analysis.MEAN)
    day_mean.convert_units('celsius')

    qplt.contourf(day_mean, 25)
    plt.gca().coastlines()
    plt.show()

def pollution_over_time():
    """
    Plots a graph of pm10 against time for a random location/model level
    """
    filename = '/data/users/ersmith/Temporary_Files/Framework/Example_Data_Files/Model/20200915_Model_Gridded_Data.nc'
    cubes = iris.load(filename)
    pm10 = iris.load_cube(filename, 'mass_concentration_of_secondary_particulate_organic_matter_in_pm10_dry_aerosol_in_air')

pollution_over_time()
