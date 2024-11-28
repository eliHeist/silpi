import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

document.addEventListener('DOMContentLoaded', () => {
    gsap.fromTo('.blur-img', 
        { 
            filter: 'blur(20px)', 
            scale: 0.9 
        },
        {
            filter: 'blur(0px)',
            scale: 1,
            scrollTrigger: {
                trigger: '.blur-img',
                start: 'top 80%',
                end: 'top 60%',
                scrub: true,
                toggleActions: 'play play reverse reverse',
            }
        }
    );
    gsap.fromTo('.slide-in-top', 
        { 
            filter: 'blur(5px)', 
            scale: 0.8,
            transform: 'translateY(200px)',
            opacity: 0
        },
        {
            filter: 'blur(0px)',
            scale: 1,
            transform: 'translateY(0%)',
            opacity: 1,
            scrollTrigger: {
                trigger: '.slide-in-top',
                start: 'top 90%',
                end: 'top 40%',
                scrub: true,
                toggleActions: 'play play reverse reverse',
            },
            stagger: 0.1,
            ease: "power1.out"
        }
    );
    gsap.fromTo('.slide-in-left', 
        { 
            filter: 'blur(5px)', 
            scale: 0.8,
            transform: 'translateX(100%)',
            opacity: 0
        },
        {
            filter: 'blur(0px)',
            scale: 1,
            transform: 'translateX(0%)',
            opacity: 1,
            scrollTrigger: {
                trigger: '.slide-in-left',
                start: 'top 90%',
                end: 'top 30%',
                scrub: true,
                toggleActions: 'play play reverse reverse',
            },
            stagger: 0.2,
            ease: "power1.out"
        }
    );
});
