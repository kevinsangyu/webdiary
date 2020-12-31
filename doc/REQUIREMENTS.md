# Requirements for WebDiary

## UI Requirements
* UR-1: The UI shall be a Web Interface on any web browser.
* UR-2: The following web pages are required:
  * UR-2.1: User registration page.
  * UR-2.2: User login page.
  * UR-2.3: Input page for:
    * UR-2.3.1: Title text input (single line)
    * UR-2.3.2: Modified date input (read-only, and auto-filled)
    * UR-2.3.3: Main text input (multiple lines)
    * UR-2.3.4: Tag input (multiple selectable items)
    * UR-2.3.5: Image input (File load from local host, multiple images shall be supported)

## User Management Requirements
* UMR-1: Users are identified by their e-mail address.
* UMR-2: Each user shall have separate data storage for their data.
* UMR-3: User information shall be protected with simple password support.
* UMR-4: User has no settings.

## Data Requirements
* DR-1: User information shall include:
  * DR-1.1: User e-mail address
  * DR-1.2: User password
* DR-2: Diary data is collection of diary entries.
* DR-3: Diary entry shall include:
  * DR-3.1: Title
  * DR-3.2: Main text
  * DR-3.3: Modified date
  * DR-3.4: Tags
  * DR-3.5: Images
