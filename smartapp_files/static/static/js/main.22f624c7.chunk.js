(this["webpackJsonpbase-app"]=this["webpackJsonpbase-app"]||[]).push([[0],{114:function(e,t,n){"use strict";n.r(t);var a=n(2),c=n(1),r=n.n(c),i=n(32),s=n.n(i),o=n(10),l=n(25),u=(n(66),n(35)),d=n(23),j=n(27),b=n.n(j),O=n(54),p=n.n(O),h=(n(74),n.p+"static/media/iconClose.12207cd1.svg"),v=n.p+"static/media/iconCloseRound.1c4d5cb3.svg",f=n.p+"static/media/iconCloudyDay.0059aebf.svg",m=n.p+"static/media/iconRainyDay.7e609283.svg",x=n.p+"static/media/iconSnowfall.282e3f04.svg",_=n.p+"static/media/iconSunny.49cd5281.svg",w=n(18),y=Object(w.a)([function(e){return e.weatherApp.weather}],(function(e){return e})),N=Object(w.a)([function(e){return e.weatherApp.cities}],(function(e){return e})),g=Object(w.a)([function(e){return e.weatherApp.city}],(function(e){return e})),S=Object(w.a)([function(e){return e.weatherApp.openSearch}],(function(e){return e})),C=n(117),E="SET_OPEN_SEARCH",k="LOAD_WEATHER",A="LOAD_WEATHER_SUCCESS",T="LOAD_CITIES",L="LOAD_CITIES_SUCCESS",D="LOAD_CITY_SUCCESS",I="LOAD_INITIAL_STATE",R=Object(C.a)(E,(function(e){return e})),W=Object(C.a)(k,(function(e){return e})),F=Object(C.a)(A,(function(e){return e})),H=Object(C.a)(T,(function(e){return e})),K=Object(C.a)(D,(function(e){return e})),M=Object(C.a)(L,(function(e){return e})),P=Object(C.a)(I),U=(n(75),Object(w.a)([function(e){return e.ui.topLoader}],(function(e){return e}))),q=Object(w.a)([function(e){return e.ui.mainLoader}],(function(e){return e}));function J(){var e=Object(o.e)(U),t=Object(c.useState)(!1),n=Object(d.a)(t,2),r=n[0],i=n[1],s=Object(c.useState)(!1),l=Object(d.a)(s,2),u=l[0],j=l[1],O=Object(c.useState)(!1),p=Object(d.a)(O,2),h=p[0],v=p[1],f=Object(c.useRef)(null),m=Object(c.useRef)(null);return Object(c.useEffect)((function(){e&&!r&&i(!0),!e&&r&&(i(!1),j(!0),f.current=setTimeout((function(){v(!0),m.current=setTimeout((function(){j(!1),v(!1)}),100)}),200))}),[e,r]),Object(c.useEffect)((function(){return function(){f.current&&clearTimeout(f.current),m.current&&clearTimeout(m.current)}}),[]),Object(a.jsx)("div",{className:b()({"top-loader":!0,"top-loader--enabled":r&&!h}),children:Object(a.jsx)("div",{className:b()({"top-loader__bar":!0,"top-loader__bar--start":r,"top-loader__bar--stop":u,"top-loader__bar--finish":h})})})}n(76);function B(){return Object(o.e)(q)?Object(a.jsx)("div",{className:"main-loader",children:Object(a.jsxs)("div",{className:"main-loader__spinner",children:[Object(a.jsx)("div",{}),Object(a.jsx)("div",{}),Object(a.jsx)("div",{}),Object(a.jsx)("div",{})]})}):null}function Y(){var e=r.a.useState(""),t=Object(d.a)(e,2),n=t[0],i=t[1],s=r.a.useRef(),l=Object(o.d)(),u=Object(o.e)(y),j=Object(o.e)(N),O=Object(o.e)(g),w=Object(o.e)(S);Object(c.useEffect)((function(){l(P())}),[l]),Object(c.useEffect)((function(){var e;w&&(null===s||void 0===s||null===(e=s.current)||void 0===e||e.focus())}),[w]);var C=p()((function(e){var t=e.target.value;t.length>=3&&!n.includes(t)&&l(H(t)),i(t)}),1e3,{leading:!0}),E=function(){!O&&w||(n.length||l(M([])),l(R(!w)))},k=function(){i(""),l(M([]))};return Object(a.jsxs)("div",{className:"app",children:[Object(a.jsx)(J,{}),Object(a.jsx)("header",{className:"app__header",children:Object(a.jsx)("button",{className:"app__btn-menu app__btn-menu--dotted",onClick:E,children:Object(a.jsx)("span",{className:"sr-only",children:"Open menu"})})}),Object(a.jsx)("main",{className:"app__main",children:O&&u&&Object(a.jsxs)("section",{className:"weather",children:[Object(a.jsx)("img",{className:"weather__icon",src:function(e){var t=e.toLowerCase();switch(!0){case t.includes("sun")||t.includes("clear"):return _;case t.includes("rain"):return m;case t.includes("snow")||t.includes("sleet"):return x;default:return f}}(u.text),alt:""}),Object(a.jsx)("strong",{className:"weather__title",children:u.text}),O&&Object(a.jsxs)(a.Fragment,{children:[Object(a.jsx)("span",{className:"weather__location",children:O}),Object(a.jsx)("div",{className:"weather__info",children:Object(a.jsxs)("div",{className:"weather-info",children:[Object(a.jsxs)("div",{className:"weather-info__item",children:[Object(a.jsxs)("strong",{className:"weather-info__title",children:[u.temp||0,"\xb0"]}),Object(a.jsx)("span",{className:"weather-info__desc",children:"Feels like"})]}),u.wind&&Object(a.jsxs)("div",{className:"weather-info__item",children:[Object(a.jsxs)("strong",{className:"weather-info__title",children:[u.wind," km/h"]}),Object(a.jsx)("span",{className:"weather-info__desc",children:"Wind speed"})]})]})})]})]})}),Object(a.jsx)("aside",{className:b()({app__aside:!0,"app__aside--show":w}),children:Object(a.jsxs)("section",{className:"weather-search",children:[Object(a.jsxs)("header",{className:"weather-search__header",children:[Object(a.jsx)("strong",{className:"weather-search__title",children:"Choose city"}),Object(a.jsx)("button",{className:"app__btn-menu weather-search__btn-close",onClick:E,children:Object(a.jsx)("img",{width:18,height:18,src:h,alt:"close"})})]}),Object(a.jsxs)("div",{className:"weather-search-input",children:[Object(a.jsx)("input",{ref:s,onChange:C,onKeyDown:function(e){"Enter"===e.key&&l(H(n))},className:"weather-search-input__field",placeholder:"Search",autoFocus:!0,value:n}),!!n.length&&Object(a.jsx)("button",{onClick:k,className:"app__btn-menu weather-search-input__btn-clear",children:Object(a.jsx)("img",{width:14,height:14,src:v,alt:"close"})})]}),Object(a.jsx)("ul",{className:"weather-search-suggestion",children:j.map((function(e){return Object(a.jsx)("li",{onClick:function(){var t;t=null===e||void 0===e?void 0:e.name,l(W(t)),k(),E()},className:"weather-search-suggestion__item",children:null===e||void 0===e?void 0:e.name},null===e||void 0===e?void 0:e.id)}))})]})}),Object(a.jsx)(B,{})]})}function z(){return Object(a.jsx)(u.c,{children:Object(a.jsx)(u.a,{path:"/",children:Object(a.jsx)(Y,{})})})}var G,Q,V=n(17),X=n(52),Z=n(55),$=n(56),ee=n(16),te=Object(ee.a)(),ne=n(13),ae=n(8),ce=n(116),re=(G={},Object(ne.a)(G,k,(function(e,t){var n=t.payload;return Object(ae.a)(Object(ae.a)({},e),{},{city:n,weather:{temp:null,wind:null,text:""}})})),Object(ne.a)(G,A,(function(e,t){var n=t.payload;return Object(ae.a)(Object(ae.a)({},e),{},{weather:Object(ae.a)({},n)})})),Object(ne.a)(G,L,(function(e,t){var n=t.payload;return Object(ae.a)(Object(ae.a)({},e),{},{cities:n})})),Object(ne.a)(G,D,(function(e,t){var n=t.payload;return Object(ae.a)(Object(ae.a)({},e),{},{city:n})})),Object(ne.a)(G,E,(function(e,t){var n=t.payload;return Object(ae.a)(Object(ae.a)({},e),{},{openSearch:n})})),G),ie=Object(ce.a)(re,{cities:[],weather:{temp:null,wind:null,text:""},city:null,openSearch:!1}),se="SET_TOP_LOADER",oe="SET_MAIN_LOADER",le=Object(C.a)(se,(function(e){return e})),ue=Object(C.a)(oe,(function(e){return e})),de=(Q={},Object(ne.a)(Q,se,(function(e,t){var n=t.payload;return Object(ae.a)(Object(ae.a)({},e),{},{topLoader:n})})),Object(ne.a)(Q,oe,(function(e,t){var n=t.payload;return Object(ae.a)(Object(ae.a)({},e),{},{mainLoader:n})})),Q),je=Object(ce.a)(de,{topLoader:!1,mainLoader:!1}),be=Object(V.combineReducers)({weatherApp:ie,ui:je,router:Object(l.b)(te)}),Oe=n(12),pe=n.n(Oe),he=n(6),ve=n(28),fe=n.n(ve),me="botx",xe="express",_e="current_weather",we="cities_autocomplete",ye="initial_state",Ne="ready",ge=pe.a.mark(ke),Se=pe.a.mark(Ae),Ce=pe.a.mark(Te),Ee=pe.a.mark(Le);function ke(e){var t,n,a,c,r,i,s,o,l,u,d,j,b,O;return pe.a.wrap((function(p){for(;;)switch(p.prev=p.next){case 0:return t=e.payload,p.prev=1,p.next=4,Object(he.c)(ue(!0));case 4:return p.next=6,fe.a.send({type:_e,handler:me,payload:{query:t}});case 6:return b=p.sent,O={temp:(null===b||void 0===b||null===(n=b.payload)||void 0===n||null===(a=n.weather)||void 0===a?void 0:a.temp_c)||(null===b||void 0===b||null===(c=b.payload)||void 0===c||null===(r=c.weather)||void 0===r?void 0:r.tempC)||null,wind:(null===b||void 0===b||null===(i=b.payload)||void 0===i||null===(s=i.weather)||void 0===s?void 0:s.wind_kph)||(null===b||void 0===b||null===(o=b.payload)||void 0===o||null===(l=o.weather)||void 0===l?void 0:l.windKph)||null,text:(null===b||void 0===b||null===(u=b.payload)||void 0===u||null===(d=u.weather)||void 0===d||null===(j=d.condition)||void 0===j?void 0:j.text)||""},p.next=10,Object(he.c)(F(O));case 10:return p.next=12,Object(he.c)(M([]));case 12:return p.next=14,Object(he.c)(R(!1));case 14:p.next=19;break;case 16:p.prev=16,p.t0=p.catch(1),console.error("loadWeatherSaga error: ".concat(p.t0.message));case 19:return p.prev=19,p.next=22,Object(he.c)(ue(!1));case 22:return p.finish(19);case 23:case"end":return p.stop()}}),ge,null,[[1,16,19,23]])}function Ae(e){var t,n;return pe.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:return t=e.payload,a.prev=1,a.next=4,Object(he.c)(le(!0));case 4:return a.next=6,fe.a.send({type:we,handler:me,payload:{query:t}});case 6:return n=a.sent,a.next=9,Object(he.c)(M(n.payload.cities));case 9:a.next=14;break;case 11:a.prev=11,a.t0=a.catch(1),console.error("loadCitiesSaga error: ".concat(a.t0.message));case 14:return a.prev=14,a.next=17,Object(he.c)(le(!1));case 17:return a.finish(14);case 18:case"end":return a.stop()}}),Se,null,[[1,11,14,18]])}function Te(){var e,t,n,a,c,r,i,s,o,l;return pe.a.wrap((function(u){for(;;)switch(u.prev=u.next){case 0:return u.prev=0,u.next=3,Object(he.c)(ue(!0));case 3:return fe.a.send({type:Ne,handler:xe}),u.next=6,fe.a.send({type:ye,handler:me,timeout:3e3});case 6:if((o=u.sent).payload.city){u.next=11;break}return u.next=10,Object(he.c)(R(!0));case 10:return u.abrupt("return");case 11:return l={temp:(null===o||void 0===o||null===(e=o.payload)||void 0===e||null===(t=e.weather)||void 0===t?void 0:t.temp_c)||(null===o||void 0===o||null===(n=o.payload)||void 0===n||null===(a=n.weather)||void 0===a?void 0:a.tempC)||null,wind:(null===o||void 0===o||null===(c=o.payload)||void 0===c||null===(r=c.weather)||void 0===r?void 0:r.wind_kph)||(null===o||void 0===o||null===(i=o.payload)||void 0===i||null===(s=i.weather)||void 0===s?void 0:s.windKph)||null,text:o.payload.weather.condition.text||""},u.next=14,Object(he.c)(K(o.payload.city));case 14:return u.next=16,Object(he.c)(F(l));case 16:u.next=23;break;case 18:return u.prev=18,u.t0=u.catch(0),console.error("loadInitialStateSaga error: ",u.t0),u.next=23,Object(he.c)(R(!0));case 23:return u.prev=23,u.next=26,Object(he.c)(ue(!1));case 26:return u.finish(23);case 27:case"end":return u.stop()}}),Ce,null,[[0,18,23,27]])}function Le(){return pe.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(he.a)([Object(he.d)(k,ke),Object(he.d)(T,Ae),Object(he.d)(I,Te)]);case 2:case"end":return e.stop()}}),Ee)}var De=pe.a.mark(Ie);function Ie(){return pe.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,Object(he.a)([Object(he.b)(Le)]);case 2:case"end":return e.stop()}}),De)}var Re=Ie;var We=function(e){var t=Object($.a)(),n=Object(X.a)(te),a=Object(V.createStore)(be,e,Object(Z.composeWithDevTools)(Object(V.applyMiddleware)(t,n)));return t.run(Re).toPromise().catch((function(e){return console.error("Saga error",e)})),a}();s.a.render(Object(a.jsx)(r.a.StrictMode,{children:Object(a.jsx)(o.a,{store:We,children:Object(a.jsx)(l.a,{history:te,children:Object(a.jsx)(z,{})})})}),document.getElementById("root"))},66:function(e,t,n){},74:function(e,t,n){},75:function(e,t,n){},76:function(e,t,n){}},[[114,1,2]]]);
//# sourceMappingURL=main.22f624c7.chunk.js.map