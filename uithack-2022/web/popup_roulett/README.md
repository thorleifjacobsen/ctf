# Popup Roulett

Enter on own risk! Hope you have McAfee installed.

motherload.td.org.uit.no:8011

# Writeup

Opening the URL shows a lot of wierd stuff. I opened up the inspector, went to sources -> search -> "UiTHack23" and there it was. 

```
sessionStorage.setItem("flag", "UiTHack23{popup-ad_engineers_needs_styling-course}");
```