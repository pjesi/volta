FCKConfig.SkinPath = FCKConfig.BasePath + 'skins/silver/';

FCKConfig.ToolbarSets['AESC_Toolbar'] = [
  ['FitWindow','Source','-','NewPage','Preview',],
  ['Cut','Copy','Paste','PasteText','PasteWord','-','Print','SpellCheck'],
  ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
  '/',
  ['Bold','Italic','Underline','StrikeThrough','-','Subscript','Superscript'],
  ['OrderedList','UnorderedList','-','Outdent','Indent','Blockquote'],
  ['JustifyLeft','JustifyCenter','JustifyRight','JustifyFull'],
  ['Link','Unlink','Anchor'],
  ['Image','Flash','Table','Rule','Smiley','SpecialChar','PageBreak'],
  '/',
  ['Style','FontFormat','FontName','FontSize'],
  ['TextColor','BGColor'],
  ['About'] // No comma for the last row.
];

FCKConfig.ImageBrowser = false;
FCKConfig.ImageUpload = false;
FCKConfig.LinkBrowser = false;