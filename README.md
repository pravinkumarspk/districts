# Tamil Nadu Districts & Taluks API

This project provides a simple, easy-to-use REST API that returns district and taluk information for the Indian state of Tamil Nadu. It’s built purely for educational and development purposes, referencing real data from official government sources.

## Live Demo

[https://tndistricts-lkv3ai896-pravinkumarspks-projects.vercel.app](https://tndistricts-lkv3ai896-pravinkumarspks-projects.vercel.app)

## Endpoints

### 1. Get All Districts with Taluks

**Endpoint:** `GET /all`  
**Returns:** All districts with their respective taluks.

**Example Response:**
```json
{
  "The Nilgiris": ["Udagamandalam", "Coonoor", "Gudalur", "Kothagiri", "Kundah", "Pandalur"],
  "Kancheepuram": ["Kancheepuram", "Kundrathur", "Sriperumbudur", "Uthiramerur", "Walajabad"]
}
```
## 2. Get All Districts
Endpoint: GET /districts
Returns: List of all districts.

### Example Response:

```json
{
  "districts": ["Chennai", "Madurai", "Salem", "..."]
}
```
## 3. Get Taluks for a District
Endpoint: GET /taluks?district_name={district}
Query Parameter: district_name (required)
Returns: Taluks under the specified district.

### Example Request:
```
/taluks?district_name=Madurai
```
### Example Response:

```json
{
  "taluks": ["Madurai North", "Madurai South", "Thiruparankundram"]
}
```
## 4. Check if Taluk Exists in a District
Endpoint: GET /check_taluk?district_name={district}&taluk_name={taluk}
Query Parameters: district_name, taluk_name
Returns: Boolean result whether match is found.

### Example Request:
```
/check_taluk?district_name=Salem&taluk_name=Yercaud
```
### Example Response:

```json
{
  "found": true
}
```
### Data Source
The dataset is collected and cleaned from the official Tamil Nadu government site. Although simplified, it’s structured to reflect actual administrative divisions as closely as possible.

### Technical Stack
 - Node.js

 - Express.js

 - Hosted on Vercel

### Usage Guidelines
 - This API is public and doesn't require authentication.

 - Ensure proper spelling when using query parameters. It’s case-insensitive but does not correct typos.

 - This is meant for development, testing, or academic use only.

### Developer Notes
 - This API was created as part of a learning initiative to build real-world backend services, handle query parameters, and deploy on serverless platforms like Vercel. Suggestions and feedback are welcome.

