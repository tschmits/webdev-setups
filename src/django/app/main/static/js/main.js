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

    // import spring transition and register
    var WallTransition = require('famous/transitions/WallTransition');
    var Transitionable   = require('famous/transitions/Transitionable');
    Transitionable.registerMethod('wall', WallTransition);

    // set golden ratio center modifier
    var phiModifier = new Modifier({
        align: [0.5, 0.381966],
    });

    // set lightbox options
    var lightboxOptions = {
        inOrigin: [0.5, 0.5],
        inOpacity: 1,
        inTransform: Transform.scale(0, 0, 1),
        inTransition: { method: 'wall', period: 300, dampingRatio: 0.3 },
        outOrigin: [0.5, 0.5],
        outOpacity: 1,
        outTransform: Transform.scale(0, 0, 1),
        outTransition: { duration: 150, curve: Easing.easeOut },
    };

    // create the main context
    var mainContext = Engine.createContext();

    var lightbox = new Lightbox(lightboxOptions);

    var slideContents = [
        '<h1 style="margin:0">Hi!</h1>',
        '<h1 style="margin:0">Welcome!</h1>',
        '<h1 style="margin:0">Click!</h1>',
    ];

    for (var i = 0; i < slideContents.length; i++) {
        var content = slideContents[i];

        var surface = new Surface({
            size: [180, 180],
            classes: ["primary-bg"],
            content: content,
            properties: {
                lineHeight: '175px',
                textAlign: 'center',
                border: '2px solid white',
                borderRadius: '90px',
                cursor: 'pointer',
            }
        });
        surface.on('click', showNextSlide);

        var view = new View();
        view.add(phiModifier).add(surface);

        slides.push(view);
    };


    mainContext.add(lightbox);

    lightbox.show(slides[0]);

    function showNextSlide(){
        index++;
        if(index >= slides.length) index = 0;
        lightbox.show(slides[index]);
    }

});
