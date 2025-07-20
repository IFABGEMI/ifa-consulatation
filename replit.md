# Consultation Ifá - Online Consultation Platform

## Overview

This is a French-language web application for Ifá consultation services called "Terre des Mystères". The platform provides users with online spiritual consultations based on the traditional Yoruba Ifá divination system. The application consists of a simple Flask backend serving static HTML pages with a sophisticated CSS design system.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Technology Stack**: Static HTML/CSS/JavaScript with Flask backend
- **Styling Framework**: Custom CSS with comprehensive CSS variables system for theming
- **Typography**: Google Fonts (Poppins family with weights 300-800)
- **Icons**: Font Awesome 6.4.0 for iconography
- **Layout**: Multi-page application with consistent design system
- **Theme Support**: Light/dark mode toggle functionality using CSS custom properties
- **Responsive Design**: Mobile-first approach with fluid layouts and flexible grid systems

### Backend Architecture
- **Framework**: Flask (Python web framework) - minimal setup
- **Server**: Development server running on port 5000, host '0.0.0.0'
- **Session Management**: Flask sessions with environment-based secret key
- **Static File Serving**: Direct file serving for HTML, CSS, images, and other assets
- **Form Handling**: Basic POST endpoint for consultation form submissions
- **Routing**: Simple route handlers for static pages and form processing

### Data Storage Solutions
- **Current State**: No database implementation - stateless application
- **Architecture**: All content served as static files
- **Form Data**: Collected but not persisted (redirects to thank you page)
- **Future Consideration**: Database integration needed for storing consultation requests and user data

## Key Components

### Design System
- **Color Palette**: 
  - Primary: Blue-purple gradient (#667eea to #764ba2)
  - Accent: Gold tones (#d4af37, #f7e98e) for highlights
  - Neutral: Sophisticated gray scale for text and backgrounds
- **Typography Scale**: Poppins font family with comprehensive weight range (300-800)
- **Shadow System**: Multi-layered shadows with different elevations for depth
- **Animation**: Smooth transitions using cubic-bezier easing functions
- **Theme System**: CSS custom properties enabling seamless light/dark mode switching

### Page Structure
- **index.html**: Main consultation request form with personal information fields
- **about.html**: Educational content about Ifá divination system and practices
- **merci.html**: Thank you confirmation page after form submission
- **Consistent Navigation**: Shared header and styling across all pages
- **Form Components**: Name, birth details, mother's name, consultation type, and question fields

### Form Processing
- **Consultation Form**: Collects personal information for spiritual consultation
- **Field Validation**: Frontend validation for required fields
- **Submission Flow**: POST to /submit endpoint, then redirect to thank you page
- **Data Fields**: Name, birth date/time/place, mother's name, consultation type, specific question

## Data Flow

1. **User Journey**: Landing page → Form completion → Submission → Thank you page
2. **Form Submission**: Client-side validation → POST request → Server processing → Redirect response
3. **Static Content**: Direct file serving for all HTML, CSS, and asset requests
4. **Navigation**: Client-side routing between static pages

## External Dependencies

### Frontend Dependencies
- **Google Fonts API**: Poppins font family loading
- **Font Awesome CDN**: Icon library (version 6.4.0)
- **No JavaScript Frameworks**: Vanilla JavaScript for interactions

### Backend Dependencies
- **Flask**: Python web framework for routing and request handling
- **Standard Library**: No additional Python packages required
- **Environment Variables**: SESSION_SECRET for session management

### Hosting Requirements
- **Python Runtime**: Flask application requires Python environment
- **Static File Serving**: Capability to serve HTML, CSS, and image files
- **Port Configuration**: Application runs on port 5000

## Deployment Strategy

### Current Setup
- **Development Mode**: Flask debug mode enabled for development
- **Host Configuration**: Binds to '0.0.0.0' for external access
- **Static Files**: Served directly from application directory
- **Environment**: Uses environment variables for configuration

### Production Considerations
- **Database Integration**: Will need database for storing consultation requests
- **Email System**: May require email service for consultation confirmations
- **Security**: Session secret should be properly configured for production
- **Static Assets**: Consider CDN for better performance
- **WSGI Server**: Replace development server with production WSGI server

### Scalability Notes
- **Current Limitations**: No data persistence, no user management
- **Future Enhancements**: Database integration, user accounts, consultation tracking
- **Performance**: Static file serving is efficient for current content-focused approach

## Recent Changes

### July 20, 2025
- **INTEGRATED FORMSPREE**: Replaced Flask form handling with Formspree service (xblkdryj)
- Form now submits directly to https://formspree.io/f/xblkdryj for email collection
- Added automatic redirect to thank you page after successful form submission
- Removed Flask /submit endpoint and simplified backend code
- **UPDATED DESIGN**: Created stunning banner design replacing simple logo
- Integrated client's new logo image within animated gradient banner
- Added floating decorative elements (stars/sparkles) with smooth animations
- Applied consistent banner design across all pages (index, about, merci)
- Made banner fully responsive for mobile and tablet devices
- **REMOVED PHOTO UPLOAD**: Removed photo upload functionality due to compatibility issues
- Photos will be handled manually during client communications instead
- Simplified form structure focusing on essential consultation information
- **MULTILINGUAL SUPPORT**: Implemented automatic language detection based on browser settings
- Added translations for French, English, and Spanish with complete form localization
- Dynamic content translation including error messages and validation text
- Fallback to French as default language for unsupported browser languages
- **ENHANCED MOBILE RESPONSIVENESS**: Improved mobile and tablet optimization
- Better touch targets and font sizing for mobile devices (prevents iOS zoom)
- Responsive navigation positioning and banner scaling for small screens
- Optimized form layouts with appropriate spacing and sizing for mobile interaction

### July 19, 2025
- **REMOVED EMAIL SECTION COMPLETELY** from consultation form for Fiverr usage
- Cleaned up JavaScript validation code removing email-related functions
- Optimized form for Fiverr client data collection (payment handled by Fiverr platform)
- Form now collects only essential consultation information: name, birth details, location, mother's name, consultation type
- **UPDATED LOGO**: Replaced with new Eye of Horus/Ifá logo (PNG format with sacred geometric patterns)
- Enhanced logo styling with multi-layered shadows and hover effects matching the green/gold theme
- Updated all pages (index, about, merci) with new logo and improved visual integration
- Maintained professional design and all modern features (gradients, animations, multilingual support)
- Confirmed form works perfectly for micro-service platforms like Fiverr

### Form Processing Status
- **✓ COMPLETED**: Formspree integration for form submissions and email delivery
- **✓ COMPLETED**: Automatic email notifications to consultation provider
- **✓ COMPLETED**: Professional form validation and user feedback
- **✓ COMPLETED**: Responsive design and beautiful banner integration

*Note: Payment processing not needed as this form is designed for Fiverr usage where payment is handled by the platform*