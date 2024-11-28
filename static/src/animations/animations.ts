import { gsap } from "gsap"
import { ScrollTrigger } from "gsap/ScrollTrigger"

export function scrollAnimations() {
    // set start values
    gsap.set(".slide-in-top", {
        y: 200,
        clipPath: 'polygon(0 0, 100% 0, 100% 0, 0 0)'
    });
    gsap.set(".slide-in-top-0", {
        y: 200,
        clipPath: 'polygon(0 0, 100% 0, 100% 0, 0 0)'
    });
    gsap.set(".slide-in-right", {
        x: -400,
        clipPath: 'polygon(100% 0, 100% 0, 100% 100%, 100% 100%)'
    });
    gsap.set(".slide-in-left", {
        x: 400,
        clipPath: 'polygon(0% 0, 0% 0, 0% 100%, 0% 100%)'
    });
    gsap.set('.fade-in', {
        opacity: 0,
    })
    gsap.set('.pop-in', {
        opacity: 0,
        scale: 0.2
    })

    // trigger to real states
    ScrollTrigger.batch('.slide-in-top', {
        onEnter: (batch:any) => {
            gsap.to(batch, {
                clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
                y: 0,
                stagger: 0.2,
                duration: .7
            })
        },
        start: '100px bottom',
        // markers: true
    })
    
    ScrollTrigger.batch('.slide-in-top-0', {
        onEnter: (batch:any) => {
            gsap.to(batch, {
                clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
                y: 0,
                stagger: 0.2,
                duration: .7
            })
        },
        start: '00px bottom',
        // markers: true
    })
    
    ScrollTrigger.batch('.slide-in-right', {
        onEnter: (batch:any) => {
            gsap.to(batch, {
                clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
                x: 0,
                stagger: 0.2,
                duration: 1
            })
        },
        start: '50% bottom',
        // markers: true
    })
    
    ScrollTrigger.batch('.slide-in-left', {
        onEnter: (batch:any) => {
            gsap.to(batch, {
                clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)',
                x: 0,
                stagger: 0.2,
                duration: 1
            })
        },
        start: '50% bottom',
        // markers: true
    })
    
    ScrollTrigger.batch('.fade-in', {
        onEnter: (batch:any) => {
            gsap.to(batch, {
                opacity: 1,
                stagger: 0.2,
                duration: 1
            })
        },
        start: '100px bottom',
        // markers: true
    })
    
    ScrollTrigger.batch('.pop-in', {
        onEnter: (batch:any) => {
            gsap.to(batch, {
                opacity: 1,
                scale: 1,
                stagger: 0.2,
                duration: .5
            })
        },
        start: '100px bottom',
        // markers: true
    })
}