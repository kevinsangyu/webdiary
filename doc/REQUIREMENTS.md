# Requirements for WebDiary

## UI Requirements
* UR-1: The UI shall be a Web Interface on any web browser.
* UR-2: The following web pages are required:
    * UR-2.1: User registration page.
    * UR-2.2: User login page.
    * UR-2.3: Diary entry input page:
        * UR-2.3.1: Title text input (single line)
        * UR-2.3.2: Modified date input (read-only, and auto-filled)
        * UR-2.3.3: Main text input (multiple lines)
        * UR-2.3.4: Tag input (multiple selectable items)
        * UR-2.3.5: Image input (File load from local host, multiple images shall be supported)
    * UR-2.4: List of Diary Entries:
        * UR-2.4.1: Following filters shall be available:
            * UR-2.4.1.1: Regular expression for title
            * UR-2.4.1.2: Regular expression for Main text
            * UR-2.4.1.3: Regular expression for Tag(s)
        * UR-2.4.2: This page shall be auto refresh when filter changed.
    * UR-2.5: Diary entry display page is same with UR-2.3: Diary entry page, with selected contents filled.

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
        * DR-3.1.1: Title is single line.
        * DR-3.1.2: Title shall be less than 256 characters.
    * DR-3.2: Main text
        * DR-3.2.1: Main text shall supoort multiple lines.
        * DR-3.2.2: And no maximum character limit.
    * DR-3.3: Modified date
        * DR-3.3.1: Modified data shall be generated from system time.
        * DR-3.3.2: User must not able to change this modified date.
    * DR-3.4: Tags
        * DR-3.4.1: Diary entry can have multiple tags.
        * DR-3.4.2: Tags shall be case-insensitive, so presented as lowercases always.
    * DR-3.5: Images
        * DR-3.5.1: Diary entry can have multiple images.
* DR-4: Diary data can be stored in any kind of DB, including normal files.
    * DR-4.1: For normal text format file, it may JSON format

