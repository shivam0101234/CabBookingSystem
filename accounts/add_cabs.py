from accounts.models import Cab

cabs = [
    ("Swift Dzire", "Rahul Sharma", "Mini", "RJ14AB1234", 15),
    ("Hyundai Aura", "Amit Verma", "Mini", "RJ14CD5678", 14),
    ("Honda Amaze", "Mohan Singh", "Sedan", "RJ14EF9012", 16),
    ("Tata Tigor", "Rakesh Yadav", "Mini", "RJ14GH3456", 13),
    ("Maruti Ciaz", "Deepak Sharma", "Sedan", "RJ14JK7890", 18),
    ("Toyota Innova", "Vikram Singh", "SUV", "RJ14LM2345", 22),
    ("Kia Carens", "Ajay Kumar", "SUV", "RJ14NO6789", 20),
    ("Mahindra XUV700", "Suresh Meena", "SUV", "RJ14PQ1234", 25),
    ("Toyota Fortuner", "Rajesh Sharma", "SUV", "RJ14RS5678", 30),
    ("Hyundai Verna", "Ankit Singh", "Sedan", "RJ14TU9012", 19),
]

for cab in cabs:
    Cab.objects.create(
        cab_name=cab[0],
        driver_name=cab[1],
        cab_type=cab[2],
        car_number=cab[3],
        price_per_km=cab[4],
        is_available=True
    )

print("✅ 10 Cabs Added Successfully!")