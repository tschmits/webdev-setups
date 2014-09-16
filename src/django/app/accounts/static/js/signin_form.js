define(function(require, exports, module) {

    var index = 0;
    var slides = [];

    // import dependencies
    var Engine        = require('famous/core/Engine');
    var Modifier      = require('famous/core/Modifier');
    var View          = require('famous/core/View');
    var Surface       = require('famous/core/Surface');
    var Transform     = require('famous/core/Transform');
    var Lightbox      = require('famous/views/Lightbox');
    var Easing        = require('famous/transitions/Easing');

    // set golden ratio center modifier
    var phiModifier = new Modifier({
        align: [0.5, 0.381966],
        origin: [0.5, 0.5],
    });

    //
    var form = document.getElementById('signin_form_container').innerHTML.replace("display:none","");
    document.getElementById('signin_form_container').remove();

    // create the main context
    var mainContext = Engine.createContext();

    var surface = new Surface({
        size: [352, 142],
        classes: ["primary-bg"],
        content: form,
        properties: {
            border: '2px solid white',
            borderRadius: '10px',
            padding: '5px'
        }
    });

    var view = new View();
    view.add(phiModifier).add(surface);

    mainContext.add(view);
});
