Vendor Profile Management and Purchase Order Tracking System Using Django and ORM

Developed a robust system for managing vendor profiles and tracking purchase orders using Django and ORM. The project includes two main components:

 ⁠1. Vendor Profile Management:
   - Model Design: Created a comprehensive model to store and manage vendor information, including fields for vendor name, contact details, address, and a unique vendor code.
   - API Endpoints:
     - POST /api/vendors/:Create new vendor profiles.
     - GET /api/vendors/:List all registered vendors.
     - GET /api/vendors/{vendor_id}/:Retrieve detailed information for a specific vendor.
     - PUT /api/vendors/{vendor_id}/:Update existing vendor details.
     - DELETE /api/vendors/{vendor_id}/:Remove vendor records from the system.

 2. Purchase Order Tracking:
   - Model Design:Developed a model to track purchase orders, incorporating fields such as PO number, vendor reference, order date, items, quantity, and status.
   - API Endpoints:
     - POST /api/purchase_orders/:Create new purchase orders.
     - GET /api/purchase_orders/:List all purchase orders, with filtering options by vendor.
     - GET /api/purchase_orders/{po_id}/:Access detailed information on specific purchase orders.
     - PUT /api/purchase_orders/{po_id}/:Modify existing purchase orders.
     - DELETE /api/purchase_orders/{po_id}/:Delete purchase orders from the system.

This project highlights expertise in API development, database management, and the implementation of CRUD functionalities, all within the Django framework.
