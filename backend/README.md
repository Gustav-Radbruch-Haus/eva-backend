# EVA SERVER

## Development Setup
* Clone the 'EVA' repositoriy ( *if not already happend* )
* Install Java 11 SDK (*at least* Java 11).
* Download and install Intellij Community Edition (Java IDE)<br>
  1.  Start Intellij and click on "Open or Import"
  2.  Navigate to your 'EVA' repository and select under: backend / *build.gradle*
  3.  Select "Open as Project" when asked how to import .. wait, gradle will fetch half of the internet as dependency.
* Install Intellij Addons ([Lombok](https://projectlombok.org/features/all) (mandatory) & [Save Actions](https://github.com/dubreuia/intellij-plugin-save-actions) (optional))<br>
  1.  Open Intellij, select preferences > plugins
  2.  Search for 'Lombok' select the plugin from the vendor 'Michail' and click install.
  3.  Search for 'Save Actions' select the plugin from the vendor 'Alexandre DuBreuil' and click install.
  4.  Restart Intellij, after restart select "enable annotation processor" when asked.

* Configure Save Actions<br>
  1.  In Intellij, select preferences > Save Actions
  2.  Under 'General' tick the first two lines<br>
        1. Activate Save Actions on save
        2. Activate Save Actions on shortcut
  3.  Under 'Formatting Options' tick the first two lines<br>
        1. Optimize Imports
        2. Reformat Files
  