// C++ program to calculate Distance 
// Between Two Points on Earth 
#include <bits/stdc++.h> 
using namespace std; 

// Utility function for 
// converting degrees to radians 
 double toRadians(const  double degree) 
{ 
	// cmath library in C++ 
	// defines the constant 
	// M_PI as the value of 
	// pi accurate to 1e-30 
	 double one_deg = (M_PI) / 180; 
	return (one_deg * degree); 
} 

double distance(double lat1, double long1, 
					double lat2, double long2) 
{ 
	// Convert the latitudes 
	// and longitudes 
	// from degree to radians. 
	lat1 = toRadians(lat1); 
	long1 = toRadians(long1); 
	lat2 = toRadians(lat2); 
	long2 = toRadians(long2); 
	
	// Haversine Formula 
	 double dlong = long2 - long1; 
	 double dlat = lat2 - lat1; 

	 double ans = pow(sin(dlat / 2), 2) + 
						cos(lat1) * cos(lat2) * 
						pow(sin(dlong / 2), 2); 

	ans = 2 * asin(sqrt(ans)); 

	// Radius of Earth in 
	// Kilometers, R = 6371 
	// Use R = 3956 for miles 
	double R = 6371; 
	
	// Calculate the result 
	ans = ans * R * 1000; 

	return ans; 
} 

// Driver Code 
int main() 
{ 
	 double lat1 = 34.040239416480794; 
	 double long1 = -81.23707064056055; 
	 double lat2 = 34.03941439358027; 
	 double long2 = -81.23535896224102; 
	
	// call the distance function 
	cout << setprecision(15) << fixed; 
	cout << distance(lat1, long1, 
					lat2, long2) << " K.M"; 

	return 0; 
} 

// This code is contributed 
// by Aayush Chaturvedi 

