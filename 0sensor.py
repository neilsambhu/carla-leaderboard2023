import carla, cv2
import numpy as np
import time
from PIL import Image

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)  # Set a timeout for network operations

world = client.get_world()
blueprint_library = world.get_blueprint_library()

# spawn_point = carla.Transform()  # Set the desired spawn location and rotation
spawn_point = world.get_map().get_spawn_points()[0]
vehicle_bp = blueprint_library.find('vehicle.audi.tt')
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

sensor_bp = blueprint_library.find('sensor.camera.rgb')
sensor_transform = carla.Transform(carla.Location(x=1.5, z=2.4))  # Set the relative position of the sensor
sensor = world.spawn_actor(sensor_bp, sensor_transform, attach_to=vehicle)

def process_sensor_data(sensor_data):
    # Access the sensor data and perform desired operations
    # image = sensor_data.as_rgb()  # Example: Convert sensor data to an RGB image
    # Process the image...
    print(type(sensor_data), sensor_data.height, sensor_data.width)
    # image_array = np.frombuffer(sensor_data.raw_data, dtype=np.dtype("uint8"))
    # print(np.shape(image_array))
    # image_array = np.reshape(image_array, (sensor_data.height, sensor_data.width, 4))
    # print(np.shape(image_array))
    # image_array = image_array[:, :, :3]  # Remove the alpha channel
    # print(type(image_array))
    
    # Access the sensor data and convert it to an RGB numpy array
    image_data = np.array(sensor_data.raw_data)
    image_bgra = image_data.reshape((sensor_data.height, sensor_data.width, 4))

    # Convert BGRA to RGB
    image_rgb = cv2.cvtColor(image_bgra, cv2.COLOR_BGRA2RGB)
    im = Image.fromarray(image_rgb)
    im.save("img.jpeg")


sensor.listen(process_sensor_data)

# Run the simulation for a specified duration
# world.tick()

# Or run the simulation for a specified number of frames
num_frames = 2
for frame in range(num_frames):
    print(f'frame {frame}')
    world.tick()

sensor.stop()  # Stop the sensor
sensor.destroy()  # Destroy the sensor
vehicle.destroy()  # Destroy the vehicle
