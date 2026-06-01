Here's the converted content formatted as a clean, professional `README.md` file:

```markdown
# BudgetBasket

A Quick Commerce Product Comparison Platform that allows users to search products across multiple grocery delivery platforms (Blinkit, Zepto, Instamart, BigBasket, etc.) and compare prices, availability, and savings in one place.

## Problem Statement

Today users manually search the same product across multiple quick-commerce applications:

- Blinkit
- Zepto
- Instamart
- BigBasket

to determine:

- Lowest price
- Best offers
- Product availability
- Delivery convenience

This process is repetitive and time-consuming.

**BudgetBasket** aims to solve this by aggregating product data from multiple platforms and presenting the best available options in a single interface.

## Current Status

### Completed

#### Backend Foundation
- FastAPI backend setup
- Modular architecture
- Environment configuration
- Middleware implementation
- Exception handling
- API versioning

#### Authentication
- User registration
- User login
- JWT authentication
- Password hashing

#### Database
- MongoDB integration
- Async database operations
- User collection
- Product collection

#### Blinkit Integration

Implemented using Playwright.

**Features:**
- Opens Blinkit search page
- Automatically sets delivery location
- Captures internal Blinkit API responses
- Extracts product data
- Supports pagination
- Returns multiple matching products

**Current status:** ✅ Working

## Planned Integrations

### Zepto
**Status:** 🟡 In Progress

**Identified:**
- Search API
- Location API
- Product response structure

**Remaining:**
- Pagination implementation
- Product parser
- Service layer

### Instamart
**Status:** ⚪ Planned

### BigBasket
**Status:** ⚪ Planned

## Tech Stack

### Backend
- FastAPI
- Python 3.12
- Uvicorn
- Pydantic
- Playwright

### Database
- MongoDB

### Authentication
- JWT
- Passlib

### Frontend (Planned)
- React
- TailwindCSS

## Project Structure

```
backend/
│
├── app/
│
├── api/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── products.py
│   │   ├── integrations.py
│   │   ├── test_db.py
│   │   └── health.py
│
├── browser/
│   └── browser_manager.py
│
├── core/
│   ├── config.py
│   ├── middleware.py
│   └── exceptions.py
│
├── db/
│   ├── mongodb.py
│   └── collections.py
│
├── integrations/
│   │
│   ├── base/
│   │   └── schemas.py
│   │
│   ├── blinkit/
│   │   ├── browser_client.py
│   │   ├── parser.py
│   │   └── service.py
│   │
│   └── zepto/
│       ├── browser_client.py
│       ├── parser.py
│       └── service.py
│
├── models/
│
├── schemas/
│
├── services/
│
└── main.py
```

## Integration Architecture

Every quick-commerce integration follows the same pattern:

```
User Search
     │
     ▼
Service Layer
     │
     ▼
Browser Client
     │
     ▼
Platform Internal API
     │
     ▼
Parser
     │
     ▼
Normalized Product Schema
```

### Common Product Schema

Every platform product is converted into:

```json
{
  "platform": "blinkit",
  "platform_product_id": "12345",
  "name": "Amul Gold Full Cream Milk",
  "image_url": "...",
  "selling_price": 72,
  "mrp": 72,
  "in_stock": true
}
```

This allows comparisons across platforms.

## Blinkit Flow

### Search
```
GET /api/v1/integrations/blinkit/search?query=milk
```

**Flow:**
1. Open Blinkit search page
2. Set delivery location
3. Capture internal API response
4. Parse products
5. Return normalized product list

**Response:**
```json
{
  "success": true,
  "platform": "blinkit",
  "query": "milk",
  "results": [...]
}
```

## API Endpoints

### Health Check
```
GET /health
```

**Response:**
```json
{
  "status": "healthy"
}
```

### Root
```
GET /
```

**Response:**
```json
{
  "message": "QuickCompare API Running"
}
```

### Blinkit Search
```
GET /api/v1/integrations/blinkit/search
```

**Query Parameters:**
- `query=milk`

**Example:**
```
GET /api/v1/integrations/blinkit/search?query=milk
```

## Installation

### Clone Repository
```bash
git clone <repository-url>
cd BudgetBasket/backend
```

### Create Virtual Environment
```bash
python -m venv venv
```

**Activate:**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Install Playwright Browsers
```bash
playwright install
```

### Environment Variables

Create `.env` file:

```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=budgetbasket

JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256

APP_NAME=BudgetBasket
```

### Run Application
```bash
uvicorn app.main:app --reload
```

**Swagger Documentation:** `http://localhost:8000/docs`

## Roadmap

### Phase 1
- ✅ Backend setup
- ✅ MongoDB integration
- ✅ Authentication
- ✅ Blinkit integration

### Phase 2
- 🟡 Zepto integration
- ⚪ Instamart integration
- ⚪ BigBasket integration

### Phase 3
- ⚪ Product comparison engine
- ⚪ Savings calculator
- ⚪ Cart optimization

### Phase 4
- ⚪ React frontend
- ⚪ User dashboards
- ⚪ Search history
- ⚪ Wishlist

### Phase 5
- ⚪ AI-powered shopping assistant
- ⚪ Smart substitutions
- ⚪ Price trend tracking

## Vision

BudgetBasket aims to become a unified quick-commerce search engine that helps users save money by instantly comparing grocery prices across all major delivery platforms.
```

This README is now properly formatted with markdown syntax, including:
- Headers of appropriate levels
- Code blocks with language specifications
- Lists (ordered and unordered)
- Status emojis (✅, 🟡, ⚪)
- Proper indentation for nested structures
- Clear section organization