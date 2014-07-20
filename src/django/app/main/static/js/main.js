define(function(require, exports, module) {

    // import dependencies
    var Engine = require('famous/core/Engine');
    var Surface = require('famous/core/Surface');
    var Modifier = require('famous/core/Modifier');

    // create the main context
    var mainContext = Engine.createContext();

    var centerModifier = new Modifier({
      origin: [0.5, 0.381966]
    });

    var surface = new Surface({
        size: [200,80],
        classes: ["red-bg"],
        content: '<h1>main.index</h1>',
        properties: {
            lineHeight: '80px',
            textAlign: 'center'
        }
    });

    mainContext.add(centerModifier).add(surface);
});
